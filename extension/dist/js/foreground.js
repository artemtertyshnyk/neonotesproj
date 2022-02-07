/******/ (() => { // webpackBootstrap
var __webpack_exports__ = {};
/*!*********************************!*\
  !*** ./assets/js/foreground.js ***!
  \*********************************/
var neonotesToken = '';
chrome.storage.sync.get(['neonotes-token'], function (res) {
  neonotesToken = res['neonotes-token'];
  console.log('token is set');

  if (!neonotesToken) {
    if (location.href !== 'http://localhost:8080/') {
      window.open('http://localhost:8080/');
    }

    neonotesToken = localStorage.getItem('neonotes-token');
    chrome.storage.sync.set({
      'neonotes-token': neonotesToken
    }, function () {});
    window.close();
  }
});
/******/ })()
;