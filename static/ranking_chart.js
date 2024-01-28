// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

console.log("ranking char")

// Area Chart Example
window.addEventListener("DOMContentLoaded", () => {
  var ctx = document.getElementById("myAreaChart");
  var myLineChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ["Wk 1", "Wk 2", "Wk 3", "Wk 4", "Wk 5", "Wk 6", "Wk 7", "Wk 8", "Wk 9", "Wk 10", "Wk 11", "Wk 12"],
      datasets: [{
        label: "Points Earned",
        lineTension: 0.3,
        backgroundColor: "rgba(0, 0, 0, 0)",
        borderColor: "rgba(2,117,216,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(2,117,216,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(2,117,216,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: [15, 5, 7, 10, 12, 8, 9, 6, 4, 3, 11, 13, 83 - (15 + 5 + 7 + 10 + 12 + 8 + 9 + 6 + 4 + 3 + 11 + 13)],
      }],
    },
    options: {
      scales: {
        xAxes: [{
          time: {
            unit: 'week'
          },
          gridLines: {
            display: false
          },
          ticks: {
            maxTicksLimit: 13 // Updated to match the number of weeks
          }
        }],
        yAxes: [{
          ticks: {
            min: 0,
            max: 20,
            maxTicksLimit: 5
          },
          gridLines: {
            color: "rgba(0, 0, 0, .125)",
          }
        }],
      },
      legend: {
        display: false
      }
    }
  });
});
