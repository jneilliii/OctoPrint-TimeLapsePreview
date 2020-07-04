# coding=utf-8
from __future__ import absolute_import

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin, settings and asset plugin. Feel free to add or remove mixins
# as necessary.
#
# Take a look at the documentation on what other plugin mixins are available.

import octoprint.plugin

class TimelapsepreviewPlugin(octoprint.plugin.AssetPlugin,
                             octoprint.plugin.TemplatePlugin):

	##~~ AssetPlugin mixin

	def get_assets(self):
		return dict(
			js=["js/timelapsepreview.js"]
		)

	##~~ Softwareupdate hook

	def get_update_information(self):
		return dict(
			timelapsepreview=dict(
				displayName="Timelapse Preview",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="jneilliii",
				repo="OctoPrint-TimeLapsePreview",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/jneilliii/OctoPrint-TimeLapsePreview/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "Timelapse Preview"
__plugin_pythoncompat__ = ">=2.7,<4" # python 2 and 3

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = TimelapsepreviewPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

