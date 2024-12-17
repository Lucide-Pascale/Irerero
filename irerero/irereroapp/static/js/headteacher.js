
    // Content switching logic
    const viewClasses = document.getElementById("view-classes");
    const addClass = document.getElementById("add-class");
    const editDeleteClass = document.getElementById("edit-delete-class");
    const studentList = document.getElementById("student-list");
    const addStudent = document.getElementById("add-student");
    const seeRecords = document.getElementById("see-records");
    const approvedTeachers = document.getElementById("approved-teachers");
    const waitingForApproval = document.getElementById("waiting-for-approval");
    const approvedParents = document.getElementById("approved-parents");
    const waitingForApprovalParents = document.getElementById("waiting-for-approval-parents");
    const lookhealthmetrics = document.getElementById("look-health-metrics");
    

    const viewClassesContent = document.getElementById("view-classes-content");
    const addClassContent = document.getElementById("add-class-content");
    const editDeleteClassContent = document.getElementById("edit-delete-class-content");
    const studentListContent = document.getElementById("student-list-content");
    const addStudentContent = document.getElementById("add-student-content");
    const seeRecordsContent = document.getElementById("see-records-content");
    const approvedTeachersContent = document.getElementById("approved-teachers-content");
    const waitingForApprovalContent = document.getElementById("waiting-for-approval-content");
    const approvedParentsContent = document.getElementById("approved-parents-content");
    const waitingForApprovalParentsContent = document.getElementById("waiting-for-approval-parents-content");

    // Function to hide all content sections
    function hideAll() {
      viewClassesContent.style.display = "none";
      addClassContent.style.display = "none";
      editDeleteClassContent.style.display = "none";
      studentListContent.style.display = "none";
      addStudentContent.style.display = "none";
      seeRecordsContent.style.display = "none";
      approvedTeachersContent.style.display = "none";
      waitingForApprovalContent.style.display = "none";
      approvedParentsContent.style.display = "none";
      waitingForApprovalParentsContent.style.display = "none";
    }

    // Event listeners to display content when clicked
    viewClasses.addEventListener("click", () => {
      hideAll();
      viewClassesContent.style.display = "block";
    });

    addClass.addEventListener("click", () => {
      hideAll();
      addClassContent.style.display = "block";
    });

    editDeleteClass.addEventListener("click", () => {
      hideAll();
      editDeleteClassContent.style.display = "block";
    });

    studentList.addEventListener("click", () => {
      hideAll();
      studentListContent.style.display = "block";
    });

    addStudent.addEventListener("click", () => {
      hideAll();
      addStudentContent.style.display = "block";
    });

    seeRecords.addEventListener("click", () => {
      hideAll();
      seeRecordsContent.style.display = "block";
    });

    approvedTeachers.addEventListener("click", () => {
      hideAll();
      approvedTeachersContent.style.display = "block";
    });

    waitingForApproval.addEventListener("click", () => {
      hideAll();
      waitingForApprovalContent.style.display = "block";
    });

    approvedParents.addEventListener("click", () => {
      hideAll();
      approvedParentsContent.style.display = "block";
    });

    waitingForApprovalParents.addEventListener("click", () => {
      hideAll();
      waitingForApprovalParentsContent.style.display = "block";
    });
  