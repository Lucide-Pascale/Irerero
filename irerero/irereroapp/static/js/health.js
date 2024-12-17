function recordMetric() {
    alert('Health metric has been recorded successfully!');
}

// Example data for health trends (e.g., weight over months)
const ctx = document.getElementById('healthTrendsChart').getContext('2d');
const healthTrendsChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
            label: 'Weight (kg)',
            data: [25, 26, 26.5, 27, 27.2, 27.5, 28, 28.2, 28.5, 28.8, 29, 29.5],
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 3,
            fill: false,
            pointRadius: 5,
            pointHoverBackgroundColor: 'rgba(75, 192, 192, 1)'
        }, {
            label: 'Height (cm)',
            data: [120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132],
            borderColor: 'rgba(153, 102, 255, 1)',
            borderWidth: 3,
            fill: false,
            pointRadius: 5,
            pointHoverBackgroundColor: 'rgba(153, 102, 255, 1)'
        }]
    },
    options: {
        responsive: true,
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Month'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Measurement'
                },
                beginAtZero: true
            }
        }
    }
});

    // const ctx = document.getElementById('healthTrendsChart').getContext('2d');
    //         const healthTrendsChart = new Chart(ctx, {
    //             type: 'line',
    //             data: {
    //                 labels: {{ labels|safe }}, // Pass list of dates/labels
    //                 datasets: [{
    //                     label: 'Metric Value',
    //                     data: {{ data|safe }}, // Pass list of values
    //                     borderColor: 'rgba(75, 192, 192, 1)',
    //                     backgroundColor: 'rgba(75, 192, 192, 0.2)',
    //                     borderWidth: 2
    //                 }]
    //             },
    //             options: {
    //                 responsive: true,
    //                 scales: {
    //                     y: { beginAtZero: true }
    //                 }
    //             }
    //         });