const information = document.getElementById('info') // Selects info tag from index.html
information.innerText = `This app is using Chrome (v${versions.chrome()}), Node.js (v${versions.node()}), and Electron (v${versions.electron()})`

const fruitsAPI = document.getElementById('fruits') //Selects tag fruits
fruitsAPI.innerText = `Here is what is given by the API call!!!!: (${JSON.parse(fruits.getFruits()).join(', ')})`