//This file allows you to explicitly define what functionalities you want exposed to the renderer from the main app


const { contextBridge } = require('electron') //Pulls the contextBridge API from the electron module
// contextBridge is the link between the renderer process and the node backend (main process)
contextBridge.exposeInMainWorld('versions', {
  node: () => process.versions.node, //Give the version of node under electron
  chrome: () => process.versions.chrome, // Give the version of Chromium browser
  electron: () => process.versions.electron // Give the version of Electron
  // we can also expose variables, not just functions
})

contextBridge.exposeInMainWorld('fruits', {
    getFruits: () => JSON.stringify(['apple', 'banana', 'cherry', 'date', 'elderberry'])
})