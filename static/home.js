$(document).ready(function() {
	$('#shoppingCart').hide();
	$('input[type="radio"]').click(function() {
		let inputValue = $(this).attr('value');
		if (inputValue == 'Unit Item') {
			$('div#weightItem').hide();
			$('div#unitItem').show();
		} else {
			$('div#unitItem').hide();
			$('div#weightItem').show();
		}
	});

	$('#nextCustomer').click(function() {
		$('input').val('');
		$('textarea').val('');
		$('input[type="radio"]').prop('checked', false);
		$('div#weightItem').show();
		$('div#unitItem').show();
	});

	$('#exit').click(function() {
		window.close();
	});

	$('#customerName').change(function(event) {
		$.ajax({
			type: 'POST',
			url: 'http://127.0.0.1:5000/selectCustomer',
			data: { name: $('#customerName').val() },
			success: function(data) {
				$('#cardNumber').val(data.cardNumber);
			}
		});
		event.preventDefault();
	});

	$('#startShopping').click(function(event) {
		$('#shoppingCart').show();
		if ($('#customerName').val() !== '' && $('#cardNumber').val() !== ''){
			$.ajax({
				type: 'POST',
				url: 'http://127.0.0.1:5000/startShopping',
				data: { name: $('#customerName').val() }
			});
			event.preventDefault();}
		else{
			alert('Invalid Input')
		}
	});

	$('#newItem').on('click', function() {
		$('#weightNumber').val('');
		$('#pricePerKilo').val('');
		$('#unitNumber').val('');
		$('#pricePerUnit').val('');
		$('#ProdName').val('');
		$('input[type="radio"]').prop('checked', false);
		$('div#weightItem').show();
		$('div#unitItem').show();
	});

	$('#addCar').click(function(event) {
		$.ajax({
			type: 'POST',
			url: '//127.0.0.1:5000/addtoCart',
			data: {
				customerName: $('#customerName').val(),
				ProdName: $('#ProdName').val(),
				pricePerUnit: $('#pricePerUnit').val(),
				unitNumber: $('#unitNumber').val(),
				pricePerKilo: $('#pricePerKilo').val()
			},
			success: function(data) {
				$('#weightNumber').val(data.weight);
				$('#checkDisplay').val(function(_, val) {
					return val + data.message + '\n';
				});
			}
		});
		event.preventDefault();
	});

	$('#checkOut').click(function(event) {
		$.ajax({
			type: 'POST',
			url: 'http://127.0.0.1:5000/checkOut',
			data: { name: $('#customerName').val() },
			success: function(data) {
				$('#cost').val('$ ' + data.totalCost);
				$('#checkDisplay').val(function(_, val) {
					return val + data.currentPoint + '\n' + data.TotalPoint;
				});
			}
		});
		event.preventDefault();
	});

	$('#total').click(function(event) {
		$.ajax({
			type: 'POST',
			url: 'http://127.0.0.1:5000/totalSales'
		});
		event.preventDefault();
	});

	$('#salesByCustomer').click(function(event) {
		$.ajax({
			type: 'POST',
			url: 'http://127.0.0.1:5000/salesByCustomer',
			success: function(data) {
				$('#display').val(function(_, val) {
					return val + data.message + '\n';
				});
			}
		});
		event.preventDefault();
	});
});
