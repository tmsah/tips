chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
	if(changeInfo.url && changeInfo.url.indexOf("zoom.us") !== -1) {
		setTimeout(function() {
			chrome.tabs.remove(tabId);
		}, 5000);
	}
});