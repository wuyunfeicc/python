var count;
function add(){
    count = document.getElementById('count').value
    count++
    document.getElementById('count').value=count
}
function dec(){
    count = document.getElementById('count').value;
    count--
    if(document.getElementById('count').value<=1){
      document.getElementsById('count').value=1
    }
    else{
        document.getElementById('count').value=count
    }
}