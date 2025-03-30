const { app, BrowserWindow } = require('electron/main');
const { spawn } = require('child_process');
require('dotenv').config();
const path = require('node:path'); //Imports the ability for pathing with node.js
const { stderr } = require('node:process');


function parseDate(dateStr) {
  const [month, day, year] = dateStr.split('/');
  return new Date(year, month - 1, day);
}
function formatDate(date) {
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  const year = date.getFullYear();
  return `${month}/${day}/${year}`;
}
function changeDate(dateStr, days) {
  const date = parseDate(dateStr);
  date.setDate(date.getDate() + days);
  return formatDate(date);
}

// Running Scraper
function runScraper(numDays, channelID) {
  const today = formatDate(new Date());
  const afterDate = changeDate(today, -numDays);
  const scraperDir = path.join(__dirname, 'DiscordChatExporter');
  
  const command = 'DiscordChatExporter.cli';
  const args = [
    'export',
    '--channel', channelID,
    '--token', process.env.DISCORD_TOKEN,
    '-f', 'csv',
    '--after', afterDate
  ];

  const child = spawn(command, args, { cwd: scraperDir, shell: true}); // spawn allows the stdout from the CLI to be output constantly

  child.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  })
  child.stderr.on('data', (data) => {
    console.log(`stderr: ${data}`);
  })
  child.on('close', (code) => {
    console.log(`Child process exited with the code ${code}`);
  })
};
runScraper(14, 874661938032943134n);

const createWindow = () => { //This is fundamentally the electron window
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
        preload: path.join(__dirname, 'preload.js') // Builds the full absolute path to preload.js in the renderer
    }
  })

  win.loadFile('index.html')
}

app.whenReady().then(() => {
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow()
    }
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})