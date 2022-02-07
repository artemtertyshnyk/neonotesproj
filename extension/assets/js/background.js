chrome.runtime.onInstalled.addListener(()=>{
    chrome.storage.sync.set({
        selectedPiece: [],
        availableNotes: []
    }, () => {});
    chrome.contextMenus.create({
       title: "Add note",
       id: "addNoteContextMenu",
        contexts: ["selection", 'image']
    });
    chrome.runtime.sendMessage({auth: 'try'})
    console.log('started!')
});
let selectedPiece= [];
let availableNotes= [];

chrome.storage.sync.get([
    'selectedPiece',
    'availableNotes'
], result => {
    selectedPiece = result.selectedPiece;
    availableNotes = result.availableNotes;
})

chrome.contextMenus.onClicked.addListener((info) => {
    let selectedText = {};
    if (info.selectionText){
        selectedText.text = info.selectionText;
    }
    if (info.srcUrl){
        selectedText.image = info.srcUrl;
    }
    chrome.storage.sync.set({
        selectedPiece: selectedText
    }, () => {
    });
});
chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
    if (msg.message == "get selection") {
        chrome.storage.sync.get(['selectedPiece'], (res) => {
            sendResponse({selection: res.selectedPiece})
        })
        return true;
    };
})


