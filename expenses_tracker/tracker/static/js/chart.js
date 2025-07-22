document.addEventListener('DOMContentLoaded', () => {
  // PIE CHART
  const pieCtx = document.getElementById('pieChart').getContext('2d');
  const pieChart = new Chart(pieCtx, {
    type: 'pie',
    data: {
      labels: Object.keys(categoryData),
      datasets: [{
        data: Object.values(categoryData),
        backgroundColor: [
          '#3498db', '#e67e22', '#9b59b6', '#1abc9c', '#f1c40f', '#ff6b6b', '#2ecc71'
        ],
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      plugins: {
        tooltip: {
          callbacks: {
            label: (tooltipItem) => {
              const label = tooltipItem.label;
              const value = tooltipItem.raw;
              return `${label}: ₹${value}`;
            }
          }
        },
        legend: {
          position: 'bottom'
        }
      }
    }
  });

  // LINE CHART
  const lineCtx = document.getElementById('lineChart').getContext('2d');
  const lineChart = new Chart(lineCtx, {
    type: 'line',
    data: {
      labels: Object.keys(trendData),
      datasets: [{
        label: 'Expense Amount',
        data: Object.values(trendData),
        fill: false,
        borderColor: '#2ecc71',
        backgroundColor: '#2ecc71',
        tension: 0.3,
        pointRadius: 4,
        pointHoverRadius: 6
      }]
    },
    options: {
      responsive: true,
      plugins: {
        tooltip: {
          callbacks: {
            label: (tooltipItem) => `₹${tooltipItem.raw}`
          }
        },
        legend: {
          display: false
        }
      },
      scales: {
        x: {
          title: {
            display: true,
            text: 'Date'
          }
        },
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: 'Amount (₹)'
          }
        }
      }
    }
  });
});
