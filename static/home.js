
$(document).ready(function() {
    $('input[type="radio"]').click(function () {
        let inputValue = $(this).attr("value");
        if (inputValue == "Unit Item") {
            $("div#weightItem").hide();
            $("div#unitItem").show();
        } else {
            $("div#unitItem").hide();
            $("div#weightItem").show();
        }
    });
});


$("#exit").click(function() {
    window.location.reload();
});


$("#newItem").click(function() {
    $("#weightNumber").val('');
    $("#pricePerKilo").val('');
    $("#unitNumber").val('');
    $("#pricePerUnit").val('');
    $("#ProdName").val('');
});

$("#customerInfo").click(function() {
    $("#display").val('Customer Info:');
});