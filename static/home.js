$(document).ready(function() {
	$('input[type="radio"]').click(function() {
		let inputValue = $(this).attr('value');
		if (inputValue == 'Unit Item') {
			$('div#weightItem').css('visibility', 'hidden');
			$('div#unitItem').css('visibility', 'visible');
		} else {
			$('div#unitItem').css('visibility', 'hidden');
			$('div#weightItem').css('visibility', 'visible');
		}
	});

	$('#nextCustomer').click(function() {
		$('input').val('');
		$('textarea').val('');
		$('input[type="radio"]').prop('checked', false);
		$('div#weightItem').css('visibility', 'visible');
		$('div#unitItem').css('visibility', 'visible');
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
		if ($('#customerName').val() !== '' && $('#cardNumber').val() !== '') {
			$.ajax({
				type: 'POST',
				url: 'http://127.0.0.1:5000/startShopping',
				data: { name: $('#customerName').val() }
			});
			event.preventDefault();
		} else {
			alert('Invalid Input');
		}
	});

	$('#customerInfo').click(function(event) {
		$.ajax({
			type: 'POST',
			url: 'http://127.0.0.1:5000/customerInfo',
			data: { customerName: $('#customerName').val() },
			success: function(data) {
				$('#display').val(data.message);
			}
		});
		event.preventDefault();
	});

	$('#newItem').click(function() {
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
					return val + data.currentPoint + '\n' + data.TotalPoint + '\n';
				});
			}
		});
		event.preventDefault();
	});

	$('#total').click(function(event) {
		$.ajax({
			type: 'POST',
			url: 'http://127.0.0.1:5000/totalSales',
			success: function(data) {
				$('#display').val(data.total);
			}
		});
		event.preventDefault();
	});

	$('#salesByCustomer').click(function(event) {
		$.ajax({
			type: 'POST',
			url: 'http://127.0.0.1:5000/salesByCustomer',
			success: function(data) {
				$('#display').val(data.message);
			}
		});
		event.preventDefault();
	});

	$('#topCustomer').click(function(event) {
		$.ajax({
			type: 'POST',
			url: 'http://127.0.0.1:5000/topCustomer',
			success: function(data) {
				$('#display').val(data.message);
			}
		});
		event.preventDefault();
	});

	$('#average').click(function(event) {
		$.ajax({
			type: 'POST',
			url: 'http://127.0.0.1:5000/averageCart',
			success: function(data) {
				$('#display').val(data.message);
			}
		});
		event.preventDefault();
	});

	$('#selectMonth').change(function(event) {
		$.ajax({
			type: 'POST',
			url: 'http://127.0.0.1:5000//monthlyDisplay',
			success: function(data) {
				$('#display').val('');
			}
		});
		event.preventDefault();
	})
});
