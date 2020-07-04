/*
 * View model for Timelapse Preview
 *
 * Author: jneilliii
 * License: MIT
 */
$(function() {
	function TimelapsepreviewViewModel(parameters) {
		var self = this;
		self.timelapseViewModel = parameters[0];

		self.selectedTimelapse = ko.observable();

		self.timelapseViewModel.show_preview = function(data){
			if(data.name.indexOf('.mp4') > 0 && self.timelapseViewModel.loginState.hasPermissionKo(self.timelapseViewModel.access.permissions.TIMELAPSE_DOWNLOAD)) {
				self.selectedTimelapse(data);
				$('#timelapse_preview').modal('show');
			} else {
				new PNotify({
					title: "Timelapse Preview",
					text: gettext("<p>Only mp4 files are supported and you must have timelapse download permissions.</p>"),
					type: "error",
					hide: true
				});
			}
		}

		self.onStartup = function(){
			$('td.timelapse_files_action, th.timelapse_files_action').css('width','60px');
			$('#timelapse_files > tbody > tr > td.timelapse_files_action').append('&nbsp;|&nbsp;<a href="javascript:void(0)" class="fa fa-camera" data-bind="click: $root.show_preview"></a>');
		}
	}

	OCTOPRINT_VIEWMODELS.push({
		construct: TimelapsepreviewViewModel,
		// ViewModels your plugin depends on, e.g. loginStateViewModel, settingsViewModel, ...
		dependencies: [ "timelapseViewModel" ],
		elements: [ "#timelapse_preview" ]
	});
});
