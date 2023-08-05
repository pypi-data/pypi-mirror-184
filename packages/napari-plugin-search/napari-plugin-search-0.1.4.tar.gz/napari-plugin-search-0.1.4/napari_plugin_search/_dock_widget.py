from napari_plugin_engine import napari_hook_implementation
from qtpy.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QListWidget, QListWidgetItem, QLabel
from qtpy.QtCore import QEvent, Qt
from magicgui import magicgui
from qtpy.QtCore import Signal, QObject, QEvent
from napari_tools_menu import register_dock_widget
from functools import lru_cache

class MyQLineEdit(QLineEdit):
    keyup = Signal()
    keydown = Signal()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.keyup.emit()
            return
        elif event.key() == Qt.Key_Down:
            self.keydown.emit()
            return
        super().keyPressEvent(event)

@register_dock_widget(menu="Utilities > Plugin search")
class PluginSearch(QWidget):
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer

        seach_field = MyQLineEdit("")
        results = QListWidget()
        results.setVisible(False)

        def text_changed(*args, **kwargs):
            search_string = seach_field.text().lower()
            results.clear()
            if len(search_string) > 0:
                results.setVisible(True)
                for plugin_name, widgets in _get_all_widgets():
                    for widget in widgets:
                        if search_string in plugin_name.lower() or search_string in widget.lower():
                            _add_result(results, plugin_name, widget)
                results.sortItems()
                self.setMaximumHeight(300)
            else:
                results.setVisible(False)
                self.setMaximumHeight(50)

        def key_up():
            if results.currentRow() > 0:
                results.setCurrentRow(results.currentRow() - 1)

        def key_down():
            if results.currentRow() < results.count() - 1:
                results.setCurrentRow(results.currentRow() + 1)

        seach_field.keyup.connect(key_up)
        seach_field.keydown.connect(key_down)
        seach_field.textChanged.connect(text_changed)
        seach_field.setMaximumHeight(30)
        self.setMaximumHeight(50)

        def item_double_clicked():
            item = results.currentItem()
            if item is not None:


                widget, widget_type = _get_widget(item.plugin_name, item.widget_name, viewer=napari_viewer)

                if widget_type == "function":
                    napari_viewer.window.add_dock_widget(magicgui(widget), area='right', name=item.plugin_name + ": " + item.widget_name)
                else:
                    napari_viewer.window.add_plugin_dock_widget(item.plugin_name, item.widget_name)

                #    napari_viewer.window.add_dock_widget(widget(), area='right')

        seach_field.returnPressed.connect(item_double_clicked)
        results.itemDoubleClicked.connect(item_double_clicked)

        self.setLayout(QVBoxLayout())

        w = QWidget()
        w.setLayout(QHBoxLayout())
        w.layout().addWidget(QLabel("Search:"))
        w.layout().addWidget(seach_field)
        self.layout().addWidget(w)

        self.layout().addWidget(results)

        w.layout().setSpacing(1)
        w.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(1)
        self.layout().setContentsMargins(3, 0, 0, 3)


def _add_result(results, plugin_name, widget_name):
    item = QListWidgetItem(widget_name + " (" + plugin_name + ")")
    item.plugin_name = plugin_name
    item.widget_name = widget_name
    results.addItem(item)


def _get_widget(plugin_name, widget_name, viewer=None):
    # try npe1
    from napari.plugins import plugin_manager
    if plugin_name in plugin_manager._function_widgets:
        functions = plugin_manager._function_widgets[plugin_name]
        if widget_name in functions:
            return functions[widget_name], "function"

    try:
        result = plugin_manager.get_widget(plugin_name, widget_name)[0], "widget"
        if result is not None:
            return result
    except:
        pass

    # try npe2
    result = get_widget_contribution(plugin_name, widget_name)
    if result is not None:
        return widget_name, "widget"


@lru_cache(maxsize=1)
def _get_all_widgets():
    all_widgets = {}

    # collect all widgets from npe1
    from napari.plugins import plugin_manager
    try:
        for hook_type, (plugin_name, widgets) in plugin_manager.iter_widgets():
            all_widgets[plugin_name] = widgets
    except:
        pass

    # collect all widgets from npe2
    try:
        import npe2
    except ImportError:
        print("Assistant skips harvesting npe2 as it's not installed.")
        return all_widgets

    pm = npe2.PluginManager.instance()

    for pname, item in pm._manifests.items():
        if item.contributions.widgets is not None:
            widgets = []
            for c in item.contributions.widgets:
                wname = c.display_name

                t = get_widget_contribution(pname, wname)
                if t is not None:
                    plugin_name = t[1]
                    widgets.append(plugin_name)
            all_widgets[pname] = widgets
    return all_widgets.items()



# source: https://github.com/napari/napari/blob/1363bd47da668a5826a75a73be93f7a7f8042fd7/napari/plugins/_npe2.py#L91
def get_widget_contribution(
        plugin_name: str, widget_name: str = None
):
    import npe2
    for contrib in npe2.PluginManager.instance().iter_widgets():
        if contrib.plugin_name == plugin_name and (
                not widget_name or contrib.display_name == widget_name
        ):
            return contrib.get_callable(), contrib.display_name
    return None

@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return [PluginSearch]
