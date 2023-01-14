Path of Exile Auto Trader

This script automates the process of "sniping" items from the market for cheap prices. As soon as a price below your threshold appears on the market, the script will send an offer to the player so long as the chat box is not restricted.

Prerequisites
1. You must have all of the required Python modules installed.
2. In the initialization section, you must change the path to your chrome profile. Simply replace the name of the profile with your profile name.
3. In the initialization section, you must change the path to your chromedriver.exe. Simply replace the path with the path to your chromedriver.exe. It is recommended to put it in the same directory indicated in the script. NOTE: Install Chromedriver from: https://chromedriver.chromium.org/downloads make sure it matches your Chrome version.
4. Set your threshold prices for chaos, divine, and mirror orbs.
5. You must have a default profile in chrome that contains cookies for your login information on https://www.pathofexile.com/. This is the profile that will be used to run the script.

Usage
1. Go to https://www.pathofexile.com/. Login and click on "Trade".
2. Search for any item with any desired characteristics.
3. Click on the "Activate Live Search" button on the top left of the page. You must copy the URL to this page to your clipboard.
4. Run the script. You should be able to select your chrome profile. Select it.
5. If you are unable to select your profile, you may need to change the ENTIRE path to your --profile-directory in the initialization section. Locate the folder of your default profile and copy the ENTIRE path.
6. Once you have selected your Chrome profile, click on the URL bar and paste the link to the live update page. Then press enter.
7. The script will now run. You can minimize the chrome window and it will continue to run in the background. It will send offers to players if their listing falls below your threshold for either of the three currencies. If you want to stop the script, simply close the chrome window.
8. If you want to change the threshold prices, you can do so in the initialization section. You will have to restart the script for the changes to take effect.

Support
If you have any questions or issues with the script, please submit them in the Issues section of this repository.
