const puppeteer = require('puppeteer');

(async () => {
	
	
	
    const browser = await puppeteer.launch({headless: true, args:['--no-sandbox', '--window-size=1000,700'/*, '--start-maximised'*/], defaultViewport: null});

  const page = await browser.newPage();
  await page.goto('http://block.hacash.org');
await page.waitFor('*')
  const textContent = await page.evaluate(() => document.querySelector('td.t1.hei').textContent);
    const textContent1 = await page.evaluate(() => document.querySelector('td.t2.gray.dts').textContent);
  const innerText = await page.evaluate(() => document.querySelector('td').innerText);
  
  


//hacdName
function hacdName() {
  const extractedElements = document.querySelectorAll('td.t2.diamond');
  const items = [];
  for (let element of extractedElements) {
    items.push(element.innerText);
  }
  return items;
}
let items = await page.evaluate(hacdName);
  

//txthash
function hacdtx() {
  const extractedElements = document.querySelectorAll('td.t5.hx');
  const items1 = [];
  for (let element of extractedElements) {
    items1.push(element.innerText);
  }
  return items1;
}
let items1 = await page.evaluate(hacdtx);



//rewards address
function rewardaddress() {
  const extractedElements = document.querySelectorAll('td.t3.addr.hd');
  const items2 = [];
  for (let element of extractedElements) {
    items2.push(element.innerText);
  }
  return items2;
}
let items2 = await page.evaluate(rewardaddress);



//feeaddress
function feeaddress() {
  const extractedElements = document.querySelectorAll('td.t4.addr.f');
  const items3 = [];
  for (let element of extractedElements) {
    items3.push(element.innerText);
  }
  return items3;
}
let items3 = await page.evaluate(feeaddress);


    
//fee offer
function feeoffer() {
  const extractedElements = document.querySelectorAll('td.t5');
  const items4 = [];
  for (let element of extractedElements) {
    items4.push(element.innerText);
  }
  return items4;
}
let items4 = await page.evaluate(feeoffer);

  
  
    
//status
function status() {
  const extractedElements = document.querySelectorAll('td.t6.stat');
  const items5 = [];
  for (let element of extractedElements) {
    items5.push(element.innerText);
  }
  return items5;
}
let items5 = await page.evaluate(status);

  
  console.log(textContent);
  console.log(textContent1);
  console.log(innerText);
  console.log(items);
	  console.log(items1);
		console.log(items2);
			console.log(items3)
				console.log(items4)
					console.log(items5)
	
  
  
  
  browser.close();
})();
