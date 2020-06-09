let b = document.querySelector('button');
PlusMinus('R1', -1);
function PlusMinus(r, pm){
    let t=document.getElementById(r);
    let v=Number(t.value);
    //alert((v+pm).toString());
    t.value = (v+pm).toString();
}
function myFunction(){
    alert('here');
    PlusMinus('R1', -1);
}
let c = document.getElementById('b1');
c.addEventListener('touchstart',myFunction,false);

b.onclick = function() {//num.toString(), Number(x4)
    switch(b.name) {
        case 'B1':
            //alert('B1');
            PlusMinus('R1', 1);
            break;
        case 'b1':
            alert('b1');
            PlusMinus('R1', -1);
            break;
        default:
            alert('wtf');
    }
    //if(b.name==='B1'){
        //PlusMinus('R1', 1);
        //let t=document.getElementById('R1');
        //t.value = '1';
    //}
}
