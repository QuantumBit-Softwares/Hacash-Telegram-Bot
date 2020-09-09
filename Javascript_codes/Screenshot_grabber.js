const puppeteer = require ("puppeteer");
const chalk = require("chalk")
//MY OCD of colorful logs for debugging
const error = chalk.bold.red
const success = chalk.keyword("green");

(async() => {
	try {
	var browser = await puppeteer.launch({headless: true, args:['--no-sandbox', '--window-size=1000,700'/*, '--start-maximised'*/], defaultViewport: null});
	
	
	//var browser = await puppeteer.launch({headless : true});
	var page = await browser.newPage();
	await page.goto('http://explorer.hacashpool.com');
	await page.waitFor(10000)
	await page.screenshot({path: "google.png"});
	await browser.close();
	console.log(success("Browser closed"));
	} catch (err) {
	console.log(error(err));
	await browser.close();
	console.log(error("Browser Closed"));
	}
	})();
