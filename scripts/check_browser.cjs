/* Optional browser checks; install test tools outside the checkout.
 * npm install --prefix /workspace/book-tools/browser epubjs@0.3.93 jszip@3.10.1 @axe-core/playwright@4.10.2
 * node scripts/check_browser.cjs
 * Requires Chromium and Playwright. Local-only server closes at completion.
 */
const fs=require('fs'),path=require('path'),http=require('http'),crypto=require('crypto');
const root=path.resolve(__dirname,'..');
const deps='/workspace/book-tools/browser/node_modules';
const {chromium}=require('/opt/codex/runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const AxeBuilder=require(path.join(deps,'@axe-core/playwright')).default;
const q=path.join(root,'quality');fs.mkdirSync(path.join(q,'screenshots'),{recursive:true});
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const reader=`<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Lokaler EPUB-Lesetest</title><style>body{margin:0}#viewer{width:100%;min-height:600px}</style></head><body><main id="viewer"></main><script src="/jszip.min.js"></script><script src="/epub.min.js"></script><script>window.readerReady=(async()=>{window.book=ePub('/book.epub');await book.ready;window.rendition=book.renderTo('viewer',{width:'100%',height:700,flow:'scrolled-doc',spread:'none',allowScriptedContent:false});await rendition.display('chapter_01.xhtml');return true;})();</script></body></html>`;
const routes={
 '/':{body:reader,type:'text/html'},
 '/epub.min.js':{file:path.join(deps,'epubjs/dist/epub.min.js'),type:'application/javascript'},
 '/jszip.min.js':{file:path.join(deps,'jszip/dist/jszip.min.js'),type:'application/javascript'},
 '/book.epub':{file:path.join(root,'output/CNC_Laser_Geschenkbox.epub'),type:'application/epub+zip'},
 '/web/index.html':{file:path.join(root,'output/web/index.html'),type:'text/html'}
};
const server=http.createServer((req,res)=>{const r=routes[new URL(req.url,'http://localhost').pathname];if(!r){res.writeHead(404);return res.end('Not found');}try{res.writeHead(200,{'Content-Type':r.type});res.end(r.body||fs.readFileSync(r.file));}catch(e){res.writeHead(500);res.end('Read failed');}});
function metricsSource(){
 const imgs=[...document.images];return {heading:document.querySelector('h1')?.textContent,headings:document.querySelectorAll('h1,h2,h3').length,navLinks:document.querySelectorAll('nav a').length,images:imgs.length,loadedImages:imgs.filter(i=>i.complete&&i.naturalWidth>0).length,brokenImages:imgs.filter(i=>!i.complete||!i.naturalWidth).map(i=>i.getAttribute('src')?.slice(0,100)),documentWidth:document.documentElement.scrollWidth,viewportWidth:document.documentElement.clientWidth,horizontalOverflow:document.documentElement.scrollWidth>document.documentElement.clientWidth+1};
}
(async()=>{
 let browser;const report={date:new Date().toISOString(),testTools:{epubjs:require(path.join(deps,'epubjs/package.json')).version,jszip:require(path.join(deps,'jszip/package.json')).version,axePlaywright:require(path.join(deps,'@axe-core/playwright/package.json')).version,playwright:require('/opt/codex/runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/package.json').version},artifacts:{epubSha256:hash(routes['/book.epub'].file),htmlSha256:hash(routes['/web/index.html'].file)},html:[],epub:[],failures:[]};
 try{
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));const base='http://127.0.0.1:'+server.address().port;
  browser=await chromium.launch({headless:true,executablePath:'/usr/bin/chromium',args:['--no-sandbox','--disable-dev-shm-usage']});report.testTools.chromium=browser.version();
  for(const width of [1280,375]){
   const context=await browser.newContext({viewport:{width,height:900}});const page=await context.newPage();await page.goto(base+'/web/index.html',{waitUntil:'networkidle'});await page.locator('img').evaluateAll(xs=>Promise.all(xs.map(i=>i.decode().catch(()=>{}))));
   const metrics=await page.evaluate(metricsSource);const nav=await page.locator('nav a').evaluateAll(xs=>xs.map(a=>({label:a.textContent,href:a.getAttribute('href'),valid:!!document.querySelector(a.getAttribute('href'))})));metrics.brokenNavigation=nav.filter(n=>!n.valid);
   const axe=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21a','wcag21aa']).analyze();metrics.axe={violations:axe.violations.map(v=>({id:v.id,impact:v.impact,description:v.description,nodes:v.nodes.length,examples:v.nodes.slice(0,3).map(n=>({target:n.target,summary:n.failureSummary}))})),incomplete:axe.incomplete.map(x=>({id:x.id,nodes:x.nodes.length})),passes:axe.passes.length};metrics.viewport=width;
   await page.screenshot({path:path.join(q,'screenshots',`web-${width}-cover.png`)});
   const chapter=page.locator('h1').filter({hasText:'5 ·'}).first();if(await chapter.count()){await chapter.scrollIntoViewIfNeeded();await page.screenshot({path:path.join(q,'screenshots',`web-${width}-chapter5.png`)});}
   if(metrics.horizontalOverflow||metrics.brokenImages.length||metrics.brokenNavigation.length)report.failures.push(`HTML ${width}: overflow/images/navigation`);
   if(metrics.axe.violations.length)report.failures.push(`HTML ${width}: ${metrics.axe.violations.length} axe rule violations`);
   report.html.push(metrics);await context.close();
  }
  for(const width of [1280,375]){
   const context=await browser.newContext({viewport:{width,height:900}});const page=await context.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message));
   await page.goto(base+'/',{waitUntil:'networkidle'});await page.evaluate(()=>window.readerReady);
   const book=await page.evaluate(()=>({spineItems:book.spine.spineItems.length,navigationItems:book.navigation.toc.length,title:book.package.metadata.title,brokenNavigation:book.navigation.toc.filter(n=>!book.spine.get(n.href)).map(n=>n.href)}));
   for(const item of ['chapter_01.xhtml','chapter_04.xhtml','chapter_05.xhtml','chapter_06.xhtml','chapter_08.xhtml','chapter_09.xhtml']){
    await page.evaluate(async item=>{await rendition.display(item)},item);
    const frame=page.frames().find(f=>f!==page.mainFrame()&&f.url().startsWith('blob:'))||page.frames().find(f=>f!==page.mainFrame());
    if(!frame)throw Error('EPUBJS did not create a reading frame');await frame.waitForSelector('h1');await frame.locator('img').evaluateAll(xs=>Promise.all(xs.map(i=>i.decode().catch(()=>{}))));const metrics=await frame.evaluate(metricsSource);
    metrics.viewport=width;metrics.spineHref=item;metrics.readerBook=book;metrics.jsErrors=[...errors];
    if(!metrics.heading||metrics.images<1||metrics.brokenImages.length||metrics.horizontalOverflow)report.failures.push(`EPUB ${width} ${item}: heading/images/overflow`);
    report.epub.push(metrics);await page.screenshot({path:path.join(q,'screenshots',`epub-${width}-${item.replace('.xhtml','')}.png`)});if(item==='chapter_05.xhtml'||item==='chapter_08.xhtml'){await frame.locator('figure').first().scrollIntoViewIfNeeded();await page.screenshot({path:path.join(q,'screenshots',`epub-${width}-${item.replace('.xhtml','')}-figure.png`)});}if(item==='chapter_04.xhtml'){await frame.locator('pre').first().scrollIntoViewIfNeeded();await page.screenshot({path:path.join(q,'screenshots',`epub-${width}-gcode.png`)});}
   }
   await context.close();
  }
 }catch(e){report.failures.push(String(e.stack||e));}
 finally{if(browser)await browser.close();await new Promise(resolve=>server.close(resolve));}
 report.passed=report.failures.length===0;fs.writeFileSync(path.join(q,'browser_review.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));if(!report.passed)process.exitCode=1;
})();
