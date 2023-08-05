import ast
import imp,os
import site

pluginFolder = site.getsitepackages()[0] +"/project/plugins"

if not os.path.isdir(pluginFolder):
    print("\nThe path to the plugin folder is incorrect: " + site.getsitepackages()[0] +"/project/plugins")
    raise SystemExit
else:

    mainFile = "__init__"

    def getAllPlugins():
        plugins = []
        possibleplugins = os.listdir(pluginFolder)
        for i in possibleplugins:
            location = os.path.join(pluginFolder, i)
            if not os.path.isdir(location) or not mainFile + ".py" in os.listdir(location):
                continue
            info = imp.find_module(mainFile, [location])
            plugins.append({"name": i, "info": info})
        return plugins

    def loadPlugin(pluginName):
        try:
            return imp.load_source(pluginName, os.path.join(pluginFolder, pluginName, mainFile + ".py"))
        except FileNotFoundError:
            return imp.load_source(pluginName, os.path.join(pluginFolder, pluginName, mainFile + ".py"))

    def getApiToken(configMap,plugin_tag):
        for plugin in configMap['plugins']:
            if plugin['plugin']+':'+plugin['tag'] == plugin_tag:
                return plugin['ApiToken']

    def getUrl(configMap,plugin_tag):
        for plugin in configMap['plugins']:
            if plugin['plugin']+':'+plugin['tag'] == plugin_tag:
                return plugin['url']

    def getPermissions(configMap, plugin_tag):
        for plugin in configMap['plugins']:
            if plugin['plugin']+':'+plugin['tag'] == plugin_tag:
                return plugin['permission']

    def getGroups(configMap,plugin_tag):
        groupsList=[]
        for plugin in configMap['plugins']:
            if plugin['plugin']+':'+plugin['tag']==plugin_tag:
                groupsList=plugin['permission']['groups']

        return groupsList

    def inviteMessage(configMap,plugin_tag):
        for plugin in configMap['plugins']:
            if plugin['plugin']+':'+plugin['tag'] == plugin_tag:
                return plugin['message_invite']

    def removalMessage(configMap,plugin_tag):
        for plugin in configMap['plugins']:
            if plugin['plugin']+':'+plugin['tag'] == plugin_tag:
                return plugin['message_remove']

    def getCLIgroups(configMap, plugin_tag, allPermissions):
        cli_groups = []
        for permission in allPermissions:
            thisPermissions = ast.literal_eval(permission)
            if thisPermissions['plugin'] == plugin_tag:
                del thisPermissions['plugin']
                return list(thisPermissions.values())
        if len(cli_groups) == 0:
            return getGroups(configMap, plugin_tag)