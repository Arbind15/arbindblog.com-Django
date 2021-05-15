// ================nav bar=================
var slt=document.getElementById("select")

var products=document.getElementById("products");

// alert("done");

function over() {
    // alert("lo");
    // document.getElementById("hiddendiv11").style.backgroundColor='red';
    // alert(document.getElementById('hiddendiv11').style.getPropertyValue("visibility"));
    document.getElementById("hiddendiv11").style.display='block';
}
function leave() {
    // products.style.color='red';
    document.getElementById("hiddendiv11").style.backgroundColor='aliceblue';
    document.getElementById("hiddendiv11").style.display='none';

}
function hidovr() {
    document.getElementById("hiddendiv11").style.display='block';
}
function hidlev() {
    document.getElementById("hiddendiv11").style.display='none';
}
function ju() {
    $('.about_par').fadeToggle();
    $('.imgdiv').datepicker();
}

function imgclk(itm) {
    // alert();
    document.getElementById('pop').style.visibility="visible";
    // document.getElementById('pop').innerText="jdsh";
    var img=document.getElementById(itm).src;
    document.getElementById('relm').src=img
    // alert(img)

}
function popc() {
    document.getElementById('pop').style.visibility="hidden";
    $('#pop').draggable();
    $
}
// alert("jju");
function detail(itm0,itm1) {
    // alert(itm1);
    var detl=document.getElementById(itm0).innerText;
    if(detl=="Show Detail")
    {
        document.getElementById(itm0).innerText="Hide Detail";
        document.getElementById(itm1).style.display="block";
        itm1='#'+itm1;
        $(itm1).fadeIn();
        // document.getElementById(itm1).style.height='200';
        // alert(itm1);
    }
    if(detl=="Hide Detail")
    {
        document.getElementById(itm0).innerText="Show Detail";
        document.getElementById(itm1).style.display="none";
        itm1='#'+itm1;
        $(itm1).fadeOut();
    }
}
function downlist() {
    alert("fd");
    // $(itm).style.visibility='hidden';
}
// $('.downlist').datepicker();
// alert("top")
var keywords;
var myvar;
function load(sr_string) {
    keywords=sr_string.split(" ");
    // alert(keywords);
    // var keywords=sr_string.split(" ");

//    since javascript has no static variable so using class to achive it
//
//     function MyClass() {
//     var privateVariable=keywords;
//     this.publicVariable=['BB'];
//     this.privilagedMethod=function () {
//
//         alert(privateVariable);
//     }
//     };
//     MyClass.prototype.publicMethod=function () {
//         alert(this.publicVariable);
//     }
//     MyClass.staticProperty=['A','k','m'];
//     // var myinstance=new MyClass();
//     myvar=new MyClass();
//     // myvar.privilagedMethod();


}


function autocom() {
    // alert(keywords);
    // myvar.privilagedMethod();
   // var keywords=["Arbind Mehta","Abhishek Thapa","India","China"];
    $('#auot_com').autocomplete({
    source:keywords
    },{});
    // alert(keywords);
}


function validate() {
    // alert("vali");
}
function edit() {
    document.getElementById('ebtn').style.visibility='hidden';
    document.getElementById('edt').style.visibility='visible';

}
function cnc() {
    document.getElementById('edt').style.visibility='hidden';
    document.getElementById('ebtn').style.visibility='visible';
}
function sav() {
    document.getElementById('edt').style.visibility='hidden';
    document.getElementById('ebtn').style.visibility='visible';
}

function changewidth1() {
    alert("d");
    // document.getElementById('hiddendiv11').style.marginRight='300px';
}
function changewidth2() {
    alert("d");
    // document.getElementById('hiddendiv11').style.marginRight='176px';
}
var x=0
function burger(flag) {
    if (x==0)
    {
        document.getElementById('navdd').style.textAlign='left';
        // document.getElementById('navdd').style.transition='transform 0.5s ease-in';
        document.getElementById('l1').style.transform='rotate(45deg)';
        document.getElementById('l2').style.opacity=0;
        document.getElementById('l3').style.transform='rotate(-45deg) translate(10px,-10px)';
        if (flag=='True')
        {
         document.getElementById('hiddendiv11').style.marginLeft='134px';
        document.getElementById('hiddendiv11').style.marginTop='-175px';
        document.getElementById('hiddendiv11').style.width='150px';
        }
        else
        {
            document.getElementById('hiddendiv11').style.marginLeft='130px';
        document.getElementById('hiddendiv11').style.marginTop='-150px';
        document.getElementById('hiddendiv11').style.width='150px';
        }

        $('#navulid').removeClass('navul');
        $('#navulid').addClass('navul1');
        $('#navdd').removeClass('navdiv');
        $('#navdd').addClass('navdiv1');
        $('#srchid').removeClass('srch');
        $('#srchid').addClass('srch1');
        $('#c1').addClass('c1');
        $('#c2').addClass('c2');
        $('#c3').addClass('c3');


        x=1;
        return;
    }
    if(x==1)
    {
        document.getElementById('l1').style.transform='rotate(0deg)';
        document.getElementById('l2').style.opacity=1;
        document.getElementById('l3').style.transform='rotate(0deg)';

        $('#navulid').addClass('navul');
        $('#navulid').removeClass('navul1');
        $('#navdd').addClass('navdiv');
        $('#navdd').removeClass('navdiv1');
        $('#srchid').removeClass('srch1');
        $('#srchid').addClass('srch');


        x=0;
        return;
    }
}

function reload() {
   document.location.reload();
}



// ---------------------Gallery--------------------------------//

// ---------------------------End of gallery----------------------------- //
