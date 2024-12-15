// JavaScript for form submission and logic
document.getElementById('attendanceForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const childName = document.getElementById('childName').value;
    const status = document.querySelector('input[name="status"]:checked') ? document.querySelector('input[name="status"]:checked').value : '';
    const remarks = document.getElementById('remarks').value;
    const attendanceDate = document.getElementById('attendanceDate').value;

    if (!status) {
        alert("Please select Present or Absent.");
        return;
    }

    // Display the status in the table
    if (childName === 'john') {
        document.getElementById('statusJohn').textContent = status;
        document.getElementById('johnDate').textContent = attendanceDate || '2024-12-15'; // Default date if no input
    } else if (childName === 'jane') {
        document.getElementById('statusJane').textContent = status;
        document.getElementById('janeDate').textContent = attendanceDate || '2024-12-15'; // Default date if no input
    } else if (childName === 'mary') {
        document.getElementById('statusMary').textContent = status;
        document.getElementById('maryDate').textContent = attendanceDate || '2024-12-15'; // Default date if no input
    }

    // Display the remarks in the table
    if (childName === 'john') {
        document.getElementById('johnRemark').textContent = remarks || 'No remarks';
    } else if (childName === 'jane') {
        document.getElementById('janeRemark').textContent = remarks || 'No remarks';
    } else if (childName === 'mary') {
        document.getElementById('maryRemark').textContent = remarks || 'No remarks';
    }

    // console.log(Child Name: ${childName});
    // console.log(Status: ${status});
    // console.log(Remarks: ${remarks});
    // console.log(Attendance Date: ${attendanceDate});

    alert("Attendance submitted successfully!");
});