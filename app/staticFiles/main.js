

  colorone();
  function colorone(){
    let ccodes = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    var menucolor = document.getElementById("menugrid");
    var a1,a2,a3,a4,a5,a6;
    a1 = ccodes[(Math.floor(Math.random()* ccodes.length))]
    a2 = ccodes[(Math.floor(Math.random()* ccodes.length))]
    a3 = ccodes[(Math.floor(Math.random()* ccodes.length))]
    a4 = ccodes[(Math.floor(Math.random()* ccodes.length))]
    a5 = ccodes[(Math.floor(Math.random()* ccodes.length))]
    a6 = ccodes[(Math.floor(Math.random()* ccodes.length))]
    menucolor.style.borderColor = `#${a1}${a2}${a3}${a4}${a5}${a6}`
   
    setTimeout(colortwo,200)
    }

    function colortwo(){
    setTimeout(colorone,200)
    }
 
 
 
 
  setTimeout(one,5000);
 function one(){
 
 fetch_data("192.168.4.1","UPDATE");

 setTimeout(two,5000)
 }
 function two(){
 fetch_data("192.168.4.1","UPDATE");
 setTimeout(one,5000)
 }


function timer(){
  var selecttime= document.getElementById('selecttime').value;
  var timeinput = document.getElementById('timeinput').value;
  var timerlabel = document.getElementById("timerlabela");
  if(selecttime=="Minutes"){
var time = parseInt(timeinput);
var sendtime = time*60; 
  }else if(selecttime=="Hours"){
    var time = parseInt(timeinput);
    var sendtime = time*60*60; 
  }else{
    var time = parseInt(timeinput);
    var sendtime = time; 
  }
  url = `192.168.4.1/TIMER=${sendtime}`;
  timerlabel.innerHTML="TIME SET SUCCESSFULLY"
  send_now(url)
}




function renamewifi(){
  var newname = document.getElementById("ssidnameinput");
  var newpword = document.getElementById("ssidpwordinput");
  var name = newname.value;
  var pword = newpword.value;
  var newurl = `192.168.4.1/ssidname=${name}&ssidpass=${pword}`;
send_now(newurl);
var label = document.getElementById("timerlabel1");
label.innerHTML = "DEVICE WIFI CHANGED SUCCESSFULLY";
}
function restart(){
  var newurl = `192.168.4.1/RESET`;
  send_now(newurl);
}
 function fetch_data(url,command_data){


 
 var http = new XMLHttpRequest();
 var url = url;
 var urlf = ""
 

 
 valid_message=`${command_data}`;
 urlf=`http://${url}/${valid_message}`;
 
 
 var params = ``;
 
 http.open('POST', urlf, true);
 
 http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
 var received = ""
 http.onreadystatechange = function() {
 if(http.readyState == 4 && http.status == 200) {
 received = http.responseText;

 


 
 var l = received.length;
 
 var d = ""
 var openbrace=0;
 var closedbrace = 0;
 var data = received;
 var character = "";
 for(var i=0; i<80; i++){
 character = data[i]
 d=d+character;
 if(character=="<"){
 openbrace=openbrace+1;
 }

 if(character==">"){
 closedbrace=closedbrace+1;
 }
 if((openbrace==2)&&(closedbrace==2)){
 break;
 }
 
 }
 var newdata = d;

 var dl = newdata.length;

 var nc = "";
 var c = "";
 var openbraced=0;
 var closedbraced = 0;
 for(var i=0;i<dl; i++){
 c = newdata[i];
 if(c==">"){
 closedbraced=closedbraced+1;
 }
 if(c=="<"){
 openbraced=openbraced+1;
 }
 if((openbraced==1)&&(closedbraced==1)&&(c!=">")){
 nc=nc+c
 }

 if((openbraced==2)&&(closedbraced==2)){
 break;
 }
 
 }
var timedisplay = document.getElementById("timedisplay");
 var switchstate2 = document.getElementById("switch");
 var s = read_d_data(nc);
 var sstate = s[1]
 var stimeleft = parseFloat(s[2])
 var menul1 = document.getElementById("menulabel1");
 var menul2 = document.getElementById("menulabel2");
 var menul3 = document.getElementById("menulabel3");
 var menul4 = document.getElementById("menulabel4");
 var menul5 = document.getElementById("menulabel5");
 var menul6 = document.getElementById("menulabel6");
 if((stimeleft >0)){
timedisplay.style.display = "inline";
timedisplay.innerHTML = `TIME LEFT:${parseInt(stimeleft)} Seconds`
if(stimeleft >= 120){
  var mins = stimeleft/60;
  timedisplay.innerHTML = `TIME LEFT:${mins.toFixed(2)} Minutes`
}
if(stimeleft >= 7200){
  var hours = stimeleft/3600;

  timedisplay.innerHTML = `TIME LEFT:${hours.toFixed(2)} Hours`
}
 }else{

  timedisplay.style.display = "none";

 }
 if((sstate=="On")||((sstate==`On`))){
 switchstate2.innerHTML = "Switch On";
menul1.style.borderColor = "#ff0000"
menul2.style.borderColor = "#ff0000"
menul3.style.borderColor = "#ff0000"
menul4.style.borderColor = "#ff0000"
menul5.style.borderColor = "#ff0000"
menul6.style.borderColor = "#ff0000"
 }else if((sstate=="Off")||(sstate==`Off`)){
 switchstate2.innerHTML = "Switch Off";
 menul1.style.borderColor = "#00CCFF"
menul2.style.borderColor = "#00CCFF"
menul3.style.borderColor = "#00CCFF"
menul4.style.borderColor = "#00CCFF"
menul5.style.borderColor = "#00CCFF"
menul6.style.borderColor = "#00CCFF"
 }
 }
 }
 http.send(params);
 }


 var ddata = document.getElementById("devicedata");
 var switchstate = document.getElementById("switch");
 var vals = ddata.innerHTML;
 function read_d_data(devicedata){
 
 var datax = devicedata;

 var x = [];
 ld = datax.length;
 var data = "";
 var dv = "";
 for(var i=0; i<ld; i++){
 dv = datax[i];
 if((dv!=",")&&(dv!="")){
 data = data + dv;
 }
 if((dv==",")||(i==ld-1)){
 if(data !=""){
 x.push(data);
 data = "";
 }
 }
 }
 
 return x; 
 }

 function switchnow(){
 
 var urlX = "127.0.0.1:5000";
 
var val = test_send(urlX);
alert(val)

 }

 function test_send(urlX){


 
    var http = new XMLHttpRequest();
    var urlf = ""
    urlf=`http://${urlX}/validate?admincode=1iloveJesus.`;
    

     var params = ``;
     
    http.open('GET', urlf, true);
    
    //http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

    http.onreadystatechange = function() {
     if(http.readyState == 4 && http.status == 200) {
      return http.responseText;
     }
     return "http.responseText";
    }
    http.send(params);
        
       
     }






 function send_now(url){
  var http = new XMLHttpRequest();
  urlf=`http://${url}`

  var params = ``;
 
  http.open('POST', urlf, true);
  
  http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
  
  http.onreadystatechange = function() {
   if(http.readyState == 4 && http.status == 200) {
  
   }
  }
  http.send(params);
   }
 function send_data(url,command_to_send,command_data){


 
var http = new XMLHttpRequest();
var url = url;
var urlf = ""

var message = command_to_send;
if(message=="switch"){
 if(command_data=="Switch Off"){
 valid_message="LED=OFF";
 urlf=`http://${url}/${valid_message}`;
 }
 if(command_data=="Switch On"){
 valid_message="LED=ON";
 urlf=`http://${url}/${valid_message}`;
 }
}

 var params = ``;
 
http.open('POST', urlf, true);

http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

http.onreadystatechange = function() {
 if(http.readyState == 4 && http.status == 200) {

 }
}
http.send(params);
 }

 var menugrid = document.getElementById("menugrid");
 var menucover = document.getElementById("menucover");
 var inmenucover2 = document.getElementById("inmenucover2");
 var inmenucover3 = document.getElementById("inmenucover3");
 var inmenucover4 = document.getElementById("inmenucover4");
 var inmenucover5 = document.getElementById("inmenucover5");
 var inmenucover6 = document.getElementById("inmenucover6");


 var menu1 = document.getElementById("menu1");
 var menu2 = document.getElementById("menu2");
 var menu3 = document.getElementById("menu3");
 var menu4 = document.getElementById("menu4");
 var menu5 = document.getElementById("menu5");
 var menu6 = document.getElementById("menu6");
 

 setTimeout(welcome,1);
 var logo = document.getElementById("logoimg");
 var caption = document.getElementById("logocaption");
 var timedisplay = document.getElementById("timedisplay");
 swidth = screen.width;
 sheight = screen.height;
 var screenratio = sheight/swidth;

 function welcome(){
 menucover.style.display = "none";
 timedisplay.style.display = "none";


 if(screenratio<1){
 menugrid.style.width = (swidth/1.1).toString()+"px";
 menugrid.style.height = (sheight/1.85).toString()+"px";
 logo.style.width = (swidth/3).toString()+"px";
 logo.style.height = (sheight/1.85).toString()+"px";
 caption.style.width = (swidth/3).toString()+"px";
 caption.style.margin = `0% ${swidth/2.8}px`;
 }
 if(screenratio>1){
 menugrid.style.width = (swidth/1.1).toString()+"px";
 
 logo.style.width = (swidth/1.85).toString()+"px";
 logo.style.height = (sheight/3).toString()+"px";
 caption.style.width = (swidth/1.5).toString()+"px";
 caption.style.margin = `0% ${swidth/4.0}px`;
 caption.style.fontSize = "100%";
 }

 
 setTimeout(menu,3000);
 }
 function menu(){
  var timedisplay = document.getElementById("timedisplay");
 var inmenucover = document.getElementById("inmenucover");
 inmenucover.style.display = "none";
 inmenucover2.style.display="none";
 inmenucover3.style.display="none";
 inmenucover4.style.display="none";
 inmenucover5.style.display="none";
 inmenucover6.style.display="none";
 menucover.style.display = "inline";
 

 
 timedisplay.style.display = "none";



 if(screenratio<1){
 logo.style.width = (swidth/30).toString()+"px";
 logo.style.height = (sheight/15).toString()+"px";
 logo.style.margin = `0% ${swidth/2}px 0% 0%`;
 caption.innerHTML = "";
 caption.style.margin = `-${sheight/230}% ${swidth/2.5}px 0px ${sheight/200}%`;
 }
 if(screenratio>1){
  var d = timedisplay.style.display;
  if(d=="none"){
   menugrid.style.height = (sheight/1.6).toString()+"px";
  }
 else{
   menugrid.style.height = (sheight/1.8).toString()+"px";
  }
 logo.style.width = (swidth/12).toString()+"px";
 logo.style.height = (sheight/25).toString()+"px";
 logo.style.margin = `0% ${swidth/2}px 0% 0%`;
 caption.innerHTML = "";
 caption.style.margin = `-${sheight/120}% ${swidth/2.8}px 0px ${swidth/100}%`;
 caption.style.fontSize = "150%";
 }
 }
 
 
 function mouseovermenu(menuid){
 var inmenucover = document.getElementById("inmenucover");
 var item = document.getElementById(menuid);

 item.style = `width:${swidth/1.3}px;height:${sheight/1.85}px;`;
 item.style.backgroundColor = "rgb(0, 119, 255);";

 
 if(menuid=="menu1"){
 var menulabel1 = document.getElementById("menulabel1");
 menulabel1.style.display = "none";
 var inmenu1 = document.getElementById("inmenu1");
 var inmenu2 = document.getElementById("inmenu2");
 var inmenu3 = document.getElementById("inmenu3");
 var inmenu4 = document.getElementById("inmenu4");
 var inmenu5 = document.getElementById("inmenu5");
 var inmenu6 = document.getElementById("inmenu6");
 var inmenu7 = document.getElementById("inmenu7");
 var inmenu8 = document.getElementById("inmenu8");
 var inmenu9 = document.getElementById("inmenu9");
 menu2.style.display = "none";
 menu3.style.display = "none";
 menu4.style.display = "none";
 menu5.style.display = "none";
 menu6.style.display = "none";


 var topleftscreen = document.getElementById("topleftscreen");
 var bottomleftscreen = document.getElementById("bottomleftscreen");
 var toprightscreen = document.getElementById("bottomrightscreen");
 var toprightscreen = document.getElementById("toprightscreen");
 var deviceinput = document.getElementById("deviceinput");

 deviceinput.style = `width:${swidth/4}px;height:${sheight/12.5}px;text-align:center;font-size:150%;font-style:bold;color:white;background-color:rgba(0, 0, 0, 0.938);display:none;`;
 inmenucover.style.display = "inline";
 var inmenu = document.getElementById("inmenu1grid");
 inmenu.style = `width:${swidth/1.3}px;height:${sheight/1.85}px;`;
 if(screenratio < 1){
  item.style = `width:${swidth/1.1}px;height:${sheight/1.9}px;border-radius:60px;margin:0% 0% 0% 0%;`;
 //item.style = `width:${swidth/1.1}px;height:${sheight/1.75}px;border-radius:60px;margin:0% 0% 0% 0%;`;
 inmenu1.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 inmenu2.style = `width:${swidth/8000.95}px;height:${sheight/2.9}px;`;
 inmenu3.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 inmenu4.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 inmenu5.style = `width:${100}%;height:${sheight/2.9}px;`;
 inmenu6.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 inmenu7.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 inmenu8.style = `width:${swidth/8000.95}px;height:${sheight/2.9}px;`;
 inmenu9.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 }
 }
 if(menuid=="menu2"){
 var menulabel2 = document.getElementById("menulabel2");
 menulabel2.style.display = "none";
 var ssisname = document.getElementById("ssidnameinput");
 var ssidpword = document.getElementById("ssidpwordinput");
 var ssidsubmit = document.getElementById("ssidsubmit");
 var timerlabel = document.getElementById("timerlabel1");

 menu1.style.display = "none";
 menu3.style.display = "none";
 menu4.style.display = "none";
 menu5.style.display = "none";
 menu6.style.display = "none";
 

 var topleftscreen = document.getElementById("topleftscreen");
 var bottomleftscreen = document.getElementById("bottomleftscreen");
 var toprightscreen = document.getElementById("bottomrightscreen");
 var toprightscreen = document.getElementById("toprightscreen");
 var deviceinput = document.getElementById("deviceinput");
 
 deviceinput.style = `width:${swidth/4}px;height:${sheight/12.5}px;text-align:center;font-size:150%;font-style:bold;color:white;background-color:rgba(0, 0, 0, 0.938);display:none;`;
 inmenucover2.style.display = "inline";

 var inmenu = document.getElementById("inmenu2grid");
 var wificontainer= document.getElementById("wificontainer");
 var inmenu2 = document.getElementById("inmenu2");
 inmenu.style = `width:${swidth/1.3}px;height:${sheight/1.85}px;`;

 if(screenratio < 1){
  item.style = `width:${swidth/1.1}px;height:${sheight/1.9}px;border-radius:10px;margin:0% 0% 0% 0%;`;
  ssisname.style = `width:48.2%;height:${sheight/14.4}px;text-align:center;`;
  ssidpword.style = `width:48.2%;height:${sheight/14.4}px; text-align:center;`;
  ssidsubmit.style = `width:99.9%;height:${sheight/14.4}px; background-color:black;color:white`;
  ssidlabel2.style = `width:99.9%;height:${sheight/14.4}px; background-color:black;color:white`;
 }
 if(screenratio > 1){
  wificontainer.style = `width:${swidth/1.5}px;height:${sheight/3.5}px;background-color:#0069a7;border:5px solid;margin:auto;padding:10px;border-color:rgb(0, 162, 255);`;
  item.style = `width:${swidth/1.1}px;height:${sheight/1.6}px;border-radius:10px;margin:-3% 0% 0% 0%;`;
  item.style.backgroundColor = "rgb(0, 119, 255);";

  inmenucover2.style = "width: 500px;";
  inmenu.style = `width:${swidth/1.3}px;height:${sheight/2.85}px;border-radius:5px;background-color:#00a2ff;border:5px solid;margin:auto;padding:10px;border-color:rgb(0, 162, 255);`;
  inmenu2.style = `width:${swidth/1.3}px;height:${sheight/2.85}px;`;
  timerlabel.style = `font-size:100%;color:white;`;
  ssisname.style = `width:${swidth/1.55}px;height:${sheight/14.4}px;text-align:center;`;
  ssidpword.style = `width:${swidth/1.55}px;height:${sheight/14.4}px; text-align:center;`;
  ssidsubmit.style = `width:${swidth/1.5}px;height:${sheight/14.4}px; background-color:black;color:white`;
  ssidlabel2.style = `width:${swidth/100.55}px;height:${sheight/1400.4}px; background-color:black;color:white`;
 
}

 }
 if(menuid=="menu3"){
 var menulabel3 = document.getElementById("menulabel3");
 var inmenu3 = document.getElementById("inmenu3");
 menulabel3.style.display = "none";
 var inputtime = document.getElementById("timeinput");
 var selecttime = document.getElementById("selecttime");
 var submittime= document.getElementById("submittime");
 var timerlabea = document.getElementById("timerlabela");
 var timercontainer = document.getElementById("timercontainer");

 menu1.style.display = "none";
 menu2.style.display = "none";
 menu4.style.display = "none";
 menu5.style.display = "none";
 menu6.style.display = "none";
 

 var topleftscreen = document.getElementById("topleftscreen");
 var bottomleftscreen = document.getElementById("bottomleftscreen");
 var toprightscreen = document.getElementById("bottomrightscreen");
 var toprightscreen = document.getElementById("toprightscreen");
 var deviceinput = document.getElementById("deviceinput");

 deviceinput.style = `width:${swidth/4}px;height:${sheight/12.5}px;text-align:center;font-size:150%;font-style:bold;color:white;background-color:rgba(0, 0, 0, 0.938);display:none;`;
 inmenucover3.style.display = "inline";
 var inmenu = document.getElementById("inmenu3grid");
 inmenu.style = `width:${swidth/1.3}px;height:${sheight/1.85}px;`;

 if(screenratio < 1){
  item.style = `width:${swidth/1.13}px;height:${sheight/1.9}px;border-radius:10px;margin:0% 0% 0% 0%;`;
  inputtime.style = `width:48.2%;height:${sheight/14.4}px;text-align:center;`;
  selecttime.style = `width:48.2%;height:${sheight/14.4}px; text-align:center;`;
  submittime.style = `width:99.9%;height:${sheight/14.4}px; background-color:black;color:white`;
  ssidlabel2.style = `width:99.9%;height:${sheight/14.4}px; background-color:black;color:white`;
 }
 if(screenratio > 1){
  timercontainer.style = `width:${swidth/1.5}px;height:${sheight/3.5}px;background-color:#0069a7;border:5px solid;margin:auto;padding:10px;border-color:rgb(0, 162, 255);`;
  item.style = `width:${swidth/1.1}px;height:${sheight/1.6}px;border-radius:10px;margin:-6% 0% 0% 0%;`;
  item.style.backgroundColor = "rgb(0, 119, 255);";

  inmenucover3.style = "width: 500px;";
  inmenu.style = `width:${swidth/1.3}px;height:${sheight/2.85}px;border-radius:5px;background-color:#00a2ff;border:5px solid;margin:auto;padding:10px;border-color:rgb(0, 162, 255);`;
  inmenu3.style = `width:${swidth/1.3}px;height:${sheight/2.85}px;`;
  timerlabela.style = `font-size:100%;color:white;`;
  inputtime.style = `width:${swidth/1.55}px;height:${sheight/14.4}px;text-align:center;`;
  selecttime.style = `width:${swidth/1.5}px;height:${sheight/14.4}px; text-align:center;`;
  submittime.style = `width:${swidth/1.5}px;height:${sheight/14.4}px; background-color:black;color:white`;

 }

 }
 if(menuid=="menu4"){
 var menulabel4 = document.getElementById("menulabel4");
 menulabel4.style.display = "none";
 var inmenu1 = document.getElementById("inmenu1");
 var inmenu2 = document.getElementById("inmenu2");
 var inmenu3 = document.getElementById("inmenu3");
 var inmenu4 = document.getElementById("inmenu4");
 var inmenu5 = document.getElementById("inmenu5");
 var inmenu6 = document.getElementById("inmenu6");
 var inmenu7 = document.getElementById("inmenu7");
 var inmenu8 = document.getElementById("inmenu8");
 var inmenu9 = document.getElementById("inmenu9");
 menu1.style.display = "none";
 menu2.style.display = "none";
 menu3.style.display = "none";
 menu5.style.display = "none";
 menu6.style.display = "none";
 

 var topleftscreen = document.getElementById("topleftscreen");
 var bottomleftscreen = document.getElementById("bottomleftscreen");
 var toprightscreen = document.getElementById("bottomrightscreen");
 var toprightscreen = document.getElementById("toprightscreen");
 var deviceinput = document.getElementById("deviceinput");

 deviceinput.style = `width:${swidth/4}px;height:${sheight/12.5}px;text-align:center;font-size:150%;font-style:bold;color:white;background-color:rgba(0, 0, 0, 0.938);display:none;`;
 inmenucover4.style.display = "inline";
 var inmenu = document.getElementById("inmenu4grid");
 inmenu.style = `width:${swidth/1.3}px;height:${sheight/1.85}px;`;
 
 inmenu1.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 inmenu2.style = `width:${swidth/8000.95}px;height:${sheight/2.9}px;`;
 inmenu3.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 inmenu4.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 inmenu5.style = `width:${100}%;height:${sheight/2.9}px;`;
 inmenu6.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 inmenu7.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 inmenu8.style = `width:${swidth/8000.95}px;height:${sheight/2.9}px;`;
 inmenu9.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 }
 if(menuid=="menu5"){
 var menulabel5 = document.getElementById("menulabel5");
 menulabel5.style.display = "none";
 var inmenu1 = document.getElementById("inmenu1");
 var inmenu2 = document.getElementById("inmenu2");
 var inmenu3 = document.getElementById("inmenu3");
 var inmenu4 = document.getElementById("inmenu4");
 var inmenu5 = document.getElementById("inmenu5");
 var inmenu6 = document.getElementById("inmenu6");
 var inmenu7 = document.getElementById("inmenu7");
 var inmenu8 = document.getElementById("inmenu8");
 var inmenu9 = document.getElementById("inmenu9");
 menu1.style.display = "none";
 menu2.style.display = "none";
 menu3.style.display = "none";
 menu4.style.display = "none";
 menu6.style.display = "none";
 

 var topleftscreen = document.getElementById("topleftscreen");
 var bottomleftscreen = document.getElementById("bottomleftscreen");
 var toprightscreen = document.getElementById("bottomrightscreen");
 var toprightscreen = document.getElementById("toprightscreen");
 var deviceinput = document.getElementById("deviceinput");

 deviceinput.style = `width:${swidth/4}px;height:${sheight/12.5}px;text-align:center;font-size:150%;font-style:bold;color:white;background-color:rgba(0, 0, 0, 0.938);display:none;`;
 inmenucover5.style.display = "inline";
 var inmenu = document.getElementById("inmenu5grid");
 inmenu.style = `width:${swidth/1.3}px;height:${sheight/1.85}px;`;
 
 inmenu1.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 inmenu2.style = `width:${swidth/8000.95}px;height:${sheight/2.9}px;`;
 inmenu3.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 inmenu4.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 inmenu5.style = `width:${100}%;height:${sheight/2.9}px;`;
 inmenu6.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 inmenu7.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 inmenu8.style = `width:${swidth/8000.95}px;height:${sheight/2.9}px;`;
 inmenu9.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 }
 if(menuid=="menu6"){
 var menulabel6 = document.getElementById("menulabel6");
 menulabel6.style.display = "none";
 var inmenu1 = document.getElementById("inmenu1");
 var inmenu2 = document.getElementById("inmenu2");
 var inmenu3 = document.getElementById("inmenu3");
 var inmenu4 = document.getElementById("inmenu4");
 var inmenu5 = document.getElementById("inmenu5");
 var inmenu6 = document.getElementById("inmenu6");
 var inmenu7 = document.getElementById("inmenu7");
 var inmenu8 = document.getElementById("inmenu8");
 var inmenu9 = document.getElementById("inmenu9");
 menu1.style.display = "none";
 menu2.style.display = "none";
 menu3.style.display = "none";
 menu4.style.display = "none";
 menu5.style.display = "none";
 

 var topleftscreen = document.getElementById("topleftscreen");
 var bottomleftscreen = document.getElementById("bottomleftscreen");
 var toprightscreen = document.getElementById("bottomrightscreen");
 var toprightscreen = document.getElementById("toprightscreen");
 var deviceinput = document.getElementById("deviceinput");

 deviceinput.style = `width:${swidth/4}px;height:${sheight/12.5}px;text-align:center;font-size:150%;font-style:bold;color:white;background-color:rgba(0, 0, 0, 0.938);display:none;`;
 inmenucover6.style.display = "inline";
 var inmenu = document.getElementById("inmenu6grid");
 inmenu.style = `width:${swidth/1.3}px;height:${sheight/1.85}px;`;
 
 inmenu1.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 inmenu2.style = `width:${swidth/8000.95}px;height:${sheight/2.9}px;`;
 inmenu3.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 inmenu4.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 inmenu5.style = `width:${100}%;height:${sheight/2.9}px;`;
 inmenu6.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 inmenu7.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 inmenu8.style = `width:${swidth/8000.95}px;height:${sheight/2.9}px;`;
 inmenu9.style = `width:${swidth/3.95}px;height:${sheight/11.1}px;`;
 }
 }
 
 
 function mouseoutmenu(menuid){
 menu1.style.display = "block";
 menu2.style.display = "block";
 menu3.style.display = "block";
 menu4.style.display = "block";
 menu5.style.display = "block";
 menu6.style.display = "block";
 
 var menulabel = document.getElementById("menulabel1");
 menulabel.style.display = "inline";
 var menulabel = document.getElementById("menulabel2");
 menulabel.style.display = "inline";
 var menulabel = document.getElementById("menulabel3");
 menulabel.style.display = "inline";
 var menulabel = document.getElementById("menulabel4");
 menulabel.style.display = "inline";
 var menulabel = document.getElementById("menulabel5");
 menulabel.style.display = "inline";
 var menulabel = document.getElementById("menulabel6");
 menulabel.style.display = "inline";
 var inmenucover = document.getElementById("inmenucover");
 inmenucover.style.display = "none";
 inmenucover2.style.display = "none";
 inmenucover3.style.display = "none";
 inmenucover4.style.display = "none";
 inmenucover5.style.display = "none";
 inmenucover6.style.display = "none";
 var inmenu = document.getElementById("inmenu1grid");
 inmenu.style.width = `width:${0}px;height:${0}px;`;
 var inmenu = document.getElementById("inmenu2grid");
 inmenu.style.width = `width:${0}px;height:${0}px;`;
 var inmenu = document.getElementById("inmenu3grid");
 inmenu.style.width = `width:${0}px;height:${0}px;`;
 var inmenu = document.getElementById("inmenu4grid");
 inmenu.style.width = `width:${0}px;height:${0}px;`;
 var inmenu = document.getElementById("inmenu5grid");
 inmenu.style.width = `width:${0}px;height:${0}px;`;
 var inmenu = document.getElementById("inmenu6grid");
 inmenu.style.width = `width:${0}px;height:${0}px;`;
 var item1 = document.getElementById("menu1");
 var item2 = document.getElementById("menu2");
 var item3 = document.getElementById("menu3");
 var item4 = document.getElementById("menu4");
 var item5 = document.getElementById("menu5");
 var item6 = document.getElementById("menu6");
 item1.style = "width:100%;height:100%;";
 item1.style.backgroundColor = "#00c2f3"
 item2.style = "width:100%;height:100%;";
 item2.style.backgroundColor = "#00c2f3";
 item3.style = "width:100%;height:100%;";
 item3.style.backgroundColor = "#00c2f3";
 item4.style = "width:100%;height:100%;";
 item4.style.backgroundColor = "#00c2f3";
 item5.style = "width:100%;height:100%;";
 item5.style.backgroundColor = "#00c2f3";
 item6.style = "width:100%;height:100%;";
 item6.style.backgroundColor = "#00c2f3";
 }
