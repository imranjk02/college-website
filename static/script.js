const courseData = {

    "bsc-it": {
        name: "B.Sc Information Technology",
        duration: "3 Years",
        eligibility: "12th Pass",
        description: "Learn programming, web development, databases, networking and modern IT technologies.",
        subjects: [
            "Programming in Python",
            "Database Management System",
            "Web Development",
            "Computer Networks",
            "Software Engineering"
        ]
    },

    "bca": {
        name: "Bachelor of Computer Applications",
        duration: "3 Years",
        eligibility: "12th Pass",
        description: "Develop computer application skills, software development knowledge and programming expertise.",
        subjects: [
            "C Programming",
            "Java Programming",
            "Data Structures",
            "Operating Systems",
            "Web Technologies"
        ]
    },

    "bcom": {
        name: "Bachelor of Commerce",
        duration: "3 Years",
        eligibility: "12th Pass",
        description: "Study accounting, finance, economics and business management.",
        subjects: [
            "Financial Accounting",
            "Business Economics",
            "Business Law",
            "Cost Accounting",
            "Taxation"
        ]
    },

    "bms": {
        name: "Bachelor of Management Studies",
        duration: "3 Years",
        eligibility: "12th Pass",
        description: "Develop business, leadership, management and entrepreneurship skills.",
        subjects: [
            "Marketing Management",
            "Human Resource Management",
            "Business Communication",
            "Financial Management",
            "Business Economics"
        ]
    }

};

const courseName = document.getElementById("courseName");

if (courseName) {

    const slug = window.location.pathname.split("/").pop();

    const course = courseData[slug];

    if (course) {

        document.getElementById("courseName").textContent =
            course.name;

        document.getElementById("courseDescription").textContent =
            course.description;

        document.getElementById("courseDuration").textContent =
            course.duration;

        document.getElementById("courseEligibility").textContent =
            course.eligibility;

        const subjectList =
            document.getElementById("courseSubjects");

        course.subjects.forEach(subject => {

            const li = document.createElement("li");

            li.textContent = subject;

            subjectList.appendChild(li);

        });

        document.getElementById("applyButton").href =
            "/register?course=" + encodeURIComponent(course.name);

    } else {

        courseName.textContent = "Course Not Found";

    }

}

const params = new URLSearchParams(window.location.search);

if (params.get("success") === "1") {

    const message = document.getElementById("registrationMessage");

    if (message) {
        message.innerHTML =
            '<div class="alert alert-success">Registration successful!</div>';
    }

}
const selectedCourse = params.get("course");

const courseSelect = document.getElementById("courseSelect");

if (selectedCourse && courseSelect) {
    courseSelect.value = selectedCourse;
}