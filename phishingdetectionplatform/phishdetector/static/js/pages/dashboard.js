//[Charts Javascript]

//Project:	Security Analytics Admin - Responsive Admin Template
//Primary use:   Used only for the Dashboard

$( document ).ready(function() {
    "use strict";
	
	new Chart(document.getElementById("line-chart1"), {
		type: 'line',
		data: {
			labels: ["May", "Jun", "July", "Aug", "Sept"],
			datasets: [{ 
				data: [100, 150, 120, 200, 180],
				label: "Total Flagged Emails",
				borderColor: "#38649f",
				fill: false
			}, { 
				data: [95, 140, 112, 150, 168],
				label: "Phishing",
				borderColor: "#D22B2B",
				fill: false
			},
			{ 
				data: [15, 110, 18, 40, 52],
				label: "Spam",
				borderColor: '#36A2EB',
				fill: false
			},
			{ 
				data: [5, 10, 8, 50, 12],
				label: "Ham",
				borderColor: "#689f38",
			}]
		},
		options: {
			title: {
			display: true,
			text: 'Threats Reported Overview'
			}
		}
	});
	
	// Bar chart
	/*new Chart(document.getElementById("bar-chart1"), {
		type: 'bar',
		data: {
		  labels: ["May", "Jun", "July", "Aug", "Sept"],
		  datasets: [
			{
			  label: "Attempts Detected",
			  backgroundColor: ["#689f38", "#38649f","#389f99","#ee1044","#ff8f00"],
			  data: [5, 10, 8, 50, 12]
			}
		  ]
		},
		options: {
		  legend: { display: false },
		  title: {
			display: true,
			text: 'Phishing Attempts Detected'
		  },
		  scales: {
			y: {
			  beginAtZero: true,
			  title: {
				display: true,
				text: 'Number of Phishing Attempts',
			  },
			},
			x: {
			  title: {
				display: true,
				text: 'Time Periods or Sources',
			  },
			},
		  },
		}
	});*/
	
	// Stacked Area chart
	if( $('#line-chart2').length > 0 ){
		var ctx1 = document.getElementById("line-chart2").getContext("2d");
		var data1 = {
			labels: ["May", "Jun", "July", "Aug", "Sept"],
			datasets: [
				{
					label: 'Viruses',
					backgroundColor: 'rgba(255, 99, 132, 0.5)',
					borderColor: 'rgba(255, 99, 132, 1)',
					borderWidth: 1,
					data: [10, 15, 8, 20, 12]
				},
				{
					label: 'Trojans',
					backgroundColor: 'rgba(54, 162, 235, 0.5)',
					borderColor: 'rgba(54, 162, 235, 1)',
					borderWidth: 1,
					data: [5, 8, 12, 6, 10]
				},
				{
					label: 'Ransomware',
					backgroundColor: 'rgba(255, 206, 86, 0.5)',
					borderColor: 'rgba(255, 206, 86, 1)',
					borderWidth: 1,
					data: [3, 6, 9, 4, 7]
				}
			]
		};
		
		var areaChart = new Chart(ctx1, {
			type:"line",
			data:data1,
			
			options: {
				tooltips: {
					mode:"label"
				},
				elements:{
					point: {
						hitRadius:90
					}
				},
				
				scales: {
					yAxes: [{
						stacked: true,
						gridLines: {
							color: "rgba(135,135,135,0)",
						},
						ticks: {
							fontFamily: "Nunito Sans",
							fontColor:"#878787"
						}
					}],
					xAxes: [{
						stacked: true,
						gridLines: {
							color: "rgba(135,135,135,0)",
						},
						ticks: {
							fontFamily: "Nunito Sans",
							fontColor:"#878787"
						}
					}]
				},
				animation: {
					duration:	3000
				},
				responsive: true,
				legend: {
					display: false,
				},
				tooltip: {
					backgroundColor:'rgba(33,33,33,1)',
					cornerRadius:0,
					footerFontFamily:"'Nunito Sans'"
				}
				
			}
		});
	}
	
	// Doughnut chart
	if( $('#doughnut-chart').length > 0 ){
		var ctx7 = document.getElementById("doughnut-chart").getContext("2d");
		var data7 = {
			 labels: [
			"Phishing",
			"Spam",
			"Ham"
		],
		datasets: [
			{
				data: [42, 41, 17],
				backgroundColor: [
					'#D22B2B', 
					'#36A2EB', 
					"#689F38", 
				],
				hoverBackgroundColor: [
					'#222222', 
					'#222222', 
					'#222222', 
				],
			}]
		};
		
		var doughnutChart = new Chart(ctx7, {
			type: 'doughnut',
			data: data7,
			options: {
				animation: {
					duration:	3000
				},
				responsive: true,
				legend: {
					labels: {
						fontFamily: "Nunito Sans",
						fontColor:"#878787"
					}
				},
				tooltip: {
					backgroundColor:'rgba(33,33,33,1)',
					cornerRadius:0,
					footerFontFamily:"'Nunito Sans'"
				},
				elements: {
					arc: {
						borderWidth: 0
					}
				},
				title: {
					display: true,
					text: 'Threat Categories Overview',
				}
			}
		});
	}
	
});