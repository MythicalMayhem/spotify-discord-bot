var asida = document.querySelector('li .asida');
asida.addEventListener('click', function a (a){
    alert(' – a sweet gruel pudding.');    })


var zgougou = document.querySelector ('li .zgougou');
zgougou.addEventListener('click', function b (b) {
    alert('– an Aleppo pine pudding.')
})

var Baklawa = document.querySelector('li .baka');
Baklawa.addEventListener('click', function c (c) {
    alert('– layers of thin pastry interspersed with ground pine nuts, etc.')
})

var Bambalouni = document.querySelector('li .bam');
Bambalouni.addEventListener('click', function d (d) {
    alert('– fried sweet donut–like cake served with sugar.')
})

var Masfouf = document.querySelector('li .masf');
Masfouf.addEventListener('click', function e (e) {
    alert('– sweetened couscous, the Tunisian version of the Moroccan seffa.')
})

document.querySelector(" .Brik").onclick=function f (f){
    var test = confirm("– tiny parcels of minced lamb, beef, or vegetables and an egg wrapped in thin pastry and deep fried.");
    if(test == true)
        window.location = "https://en.wikipedia.org/wiki/Brik";
};

document.querySelector(" .Chorba").onclick=function g (g){
    alert("– a seasoned broth, with pasta, meatballs, fish, etc.");
    window.location= "https://fr.wikipedia.org/wiki/Chorba";
};

document.querySelector(" .Kamounia").onclick=function h (h){
    alert("– a beef and cumin stew");
    window.location= "https://fr.wikipedia.org/wiki/Kamounia";
};

document.querySelector(" .Merguez").onclick=function i (i){
    alert(" – small spicy sausages.");
    window.location= "https://fr.wikipedia.org/wiki/Merguez";
};