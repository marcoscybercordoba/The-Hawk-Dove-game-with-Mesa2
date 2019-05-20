// HistogramModule.js
		var HistogramModule = function(bins, canvas_width, canvas_height) {
		    var canvas_tag = "<canvas width='" + canvas_width + "' height='" + canvas_height + "' ";
		    canvas_tag += "style='border:1px dotted'></canvas>";
		    var canvas = $(canvas_tag)[0];
		    $("body").append(canvas);
		    var context = canvas.getContext("2d");

		bins = [
			"SiempreEscala Grande",
			"SiempreEscala Chico",
			"NuncaEscala Grande",
			"NuncaEscala Chico",
			"EscalaSiElOtroEsMasGrande Grande",
			"EscalaSiElOtroEsMasGrande Chico",
			]

        dataNew = [
			10,
			23,
			10,
			23,
			10,
			23,
			]

		var datos = {
			type: "pie",
			data : {
				datasets :[{
					data : dataNew,
					backgroundColor: [
						"#08088A",
						"#5858FA",
						"#8A0829",
						"#FA5882",
						"#868A08",
						"#F2F5A9",
					],
				}],
				labels : bins
			},
			options : {
				responsive : true,
			}
		};



	        var chart = new Chart(context, datos);


	        for (var i in dataNew) {
                    //alert(chart.data.datasets[0].data[i])
	                chart.data.datasets[0].data[i] = 6;
            }
	        chart.update();


	        this.render = function(data) {
        	   for (var i in data) {
                    //alert(chart.data.datasets[0].data[i])
	                chart.data.datasets[0].data[i] = data[i];
               }
      	       chart.update();
    	     };

		    
	     };

	     //alert("c1")
	     //var hist1 = new HistogramModule(10, 200, 500)
