
        // Sample student data
        const students = [
            
            
            { name: "Habimana Moise", age: 9, description: "Moise loves drawing and is a very artistic student.", health: "Healthy, no issues.", status: "Good", image:  "./images/child1.png", id: 1 },
            { name: "Iraguha Marthe", age: 9, description: "Marthe loves drawing and is a very artistic student.", health: "Healthy, no issues.", status: "Good", image: "./images/child2.jpg", id: 2 },
            { name: "Muzima J.Aime", age: 9, description: "Aime loves drawing and is a very artistic student.", health: "Healthy, no issues.", status: "Good", image:  "./images/child3.png", id: 3 },
            { name: "Gikundiro Denyse", age: 9, description: "Denyse loves drawing and is a very artistic student.", health: "Healthy, no issues.", status: "Good", image:  "./images/child4.png", id: 4 },
            { name: "Abayisenga Vanessa", age: 9, description: "Vanessa loves drawing and is a very artistic student.", health: "Healthy, no issues.", status: "Good", image: "./images/child5.png", id: 5 },
            { name: "Manzi Arsene", age: 9, description: "Manzi loves drawing and is a very artistic student.", health: "Healthy, no issues.", status: "Good", image:  "./images/child6.jpg", id: 6 },
            { name: "Murenzi William", age: 9, description: "Murenzi loves drawing and is a very artistic student.", health: "Healthy, no issues.", status: "Good", image:  "./images/child7.jpg", id: 7 },
            { name: "Mutamba Ines", age: 9, description: "Ines loves drawing and is a very artistic student.", health: "Healthy, no issues.", status: "Good", image: "./images/child8.jpg", id: 8 },
            { name: "Kaneza olga", age: 9, description: "Olga loves drawing and is a very artistic student.", health: "Healthy, no issues.", status: "Good", image:  "./images/child9.jpg", id: 9 },
        ];

        // Function to display all students
        function displayAllStudents() {
            const studentList = document.getElementById("student-list");
            studentList.innerHTML = ""; // Clear any previous content

            students.forEach(student => {
                const statusClass = student.status === "Good" ? "active-status" : "";
                const statusText = student.status === "Good" ? "Good Health" : "";
                const bullet = student.status === "Good" ? "<span style='color: blue;'>•</span>" : "";
                const listItem = document.createElement("li");
                listItem.innerHTML = `
                    <div style="position: relative;">
                        <img src="${student.image}" alt="${student.name}" />
                        <div class="overlay">
                            <h3>${student.name}</h3>
                            <p>Age: ${student.age}</p>
                        </div>
                    </div>
                    <p>${student.description}</p>
                    <p class="status">${bullet} ${statusText}</p>
                    <button onclick="showStudentDetails(${student.id})">More Info</button>
                `;
                studentList.appendChild(listItem);
            });
        }

        // Function to show student details
        function showStudentDetails(studentId) {
            const student = students.find(s => s.id === studentId);
            if (student) {
                alert(`${student.name}: ${student.health}`);
            }
        }

       

        // Display all students on page load
        displayAllStudents();
    