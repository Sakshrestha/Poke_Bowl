
// isotope js
$(window).on('load', function () {
    $('.filters_menu li').click(function () {
        $('.filters_menu li').removeClass('active');
        $(this).addClass('active');

        var data = $(this).attr('data-filter');
        $grid.isotope({
            filter: data
        })
    });

    var $grid = $(".grid").isotope({
        itemSelector: ".all",
        percentPosition: false,
        masonry: {
            columnWidth: ".all"
        }
    })
    
});

$(document).ready(function() {
    $(".dropdown-toggle").dropdown();
    $('#rateMe3').mdbRate();
});


// nice select
$(document).ready(function() {
    $('select').niceSelect();
  });





function ModelFunction(price){
    
    document.getElementById('model').style.display='block';
    document.getElementById('item_price').innerHTML = price ;
    document.getElementById('hidden_price').value = price;
    updatePrice();
}

function updatePrice() {
    let base_price = parseFloat(document.getElementById("hidden_price").value);
    const ingredients = new Array()
    const checkboxes = document.getElementsByClassName("item");
    for(let i = 0; i < checkboxes.length; i++) {
        if(checkboxes[i].checked){ 
            base_price += parseFloat(checkboxes[i].value) || 0;
            ingredients.push(checkboxes[i].id)
    }
} 
    
    document.getElementById("item_price").innerText = base_price;
}

