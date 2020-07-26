$(document).ready(function(){
	$('#submit').click(function(e){
		e.preventDefault();
		var present_price		= $('#present_price').val();
		var kms_driven			= $('#kms_driven').val();
		var owner				= $('#owner').val();
		var year				= $('#year').val();

		var fuel_type			= $("input[name='fuel_type']:checked"). val();
		var seller_type			= $("input[name='seller_type']:checked"). val();
		var transmission_type	= $("input[name='transmission_type']:checked"). val();

		var user_data = JSON.stringify({
			'present_price':present_price,
			'kms_driven':kms_driven,
			'owner':owner,
			'year':year,
			'fuel_type':fuel_type,
			'seller_type':seller_type,
			'transmission_type':transmission_type
		});

		$.ajax({
			type:'POST',
			url:'/predictPrice',
			dataType: 'json',
			contentType:'application/json',
			data:user_data,
			success:function(response){
				var predicted_price = 'Predicted Selling Price: <strong>Rs. '+response['predicted_price']+' Lakh</strong>';

				$('#div_msg').removeClass( "error" ).addClass( "success" );
				$('#div_msg').html(predicted_price);
			},
			error:function(e){
				$('#div_msg').removeClass( "success" ).addClass( "error" );
				$('#div_msg').html('Error: something went wrong.');

				setTimeout(function(){
					$('#div_msg').removeClass('error');
					$('#div_msg').html('&nbsp;');
				}, 5000);

			}
		});
	});
});