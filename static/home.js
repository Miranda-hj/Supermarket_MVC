$(document).ready(function() {

	$('div#transcation input').prop('disabled', true);
	$('div#transcation button').prop('disabled', true);
	$('div#weightItem').css('visibility', 'hidden');
	$('div#unitItem').css('visibility', 'hidden');

	$('#nextCustomer').click(function(){
		$('#cardNumber').val('')
		$('#checkDisplay').val('');
		$('#weightNumber').val('');
		$('#pricePerKilo').val('');
		$('#unitNumber').val('');
		$('#pricePerUnit').val('');
		$('#ProdName').val('');
		$('input[type="radio"]').prop('checked', false);
		$('div#weightItem').css('visibility', 'hidden');
		$('div#unitItem').css('visibility', 'hidden');
		$('div#transcation input').prop('disabled', true);
		$('div#transcation button').prop('disabled', true);
	});
	
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
				data: { name: $('#customerName').val() },
				success:function(){
					$('div#transcation input').prop('disabled', false);
					$('div#transcation button').prop('disabled', false);
				}
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
		$('div#weightItem').css('visibility', 'hidden');
		$('div#unitItem').css('visibility', 'hidden');
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
			},
			error: function(xhr, textStatus, errorThrown){
				alert('Invalid Input')
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
				if (data.totalCost !== 0) {
					$('#cost').val('$ ' + data.totalCost);
					$('#checkDisplay').val(function(_, val) {
						return val + data.currentPoint + '\n' + data.TotalPoint + '\n';
					});
				}
				else {
					alert('Invalid Input')
				}
			}
		});
		event.preventDefault();
	});

	$('#total').click(function(event) {
		$.ajax({
			type: 'POST',
			url: 'http://127.0.0.1:5000/totalSales',
			success: function(data) {
				$('#display').val('Total Sales: $' + data.total);
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
		month = $('#selectMonth').val().split('-');
		formatMonth = `${month[1]}/${month[0]}`;
		$.ajax({
			type: 'POST',
			url: 'http://127.0.0.1:5000//monthlyDisplay',
			data: {month: formatMonth},
			success: function(data) {
				$('#display').val(data.message);
			}
		});
		event.preventDefault();
	})
});
