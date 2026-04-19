const token = localStorage.getItem("access");

if (!token) {
    // اگر لاگین نکرده بود برگرد به لاگین
    window.location.href = "/login/";
}

document.getElementById("logout").addEventListener("click", () => {
    localStorage.removeItem("access");
    window.location.href = "/login/";
});


document.addEventListener("DOMContentLoaded", async () => {

    const token = localStorage.getItem("access");

    if (!token) {
        window.location.href = "/login/";
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/users/user/info/", {
            
            headers: {
                "Authorization": `Bearer ${token}`
            }
        });

        const data = await response.json();
        // 🎯 این قسمت مرحله ۱ ماست
        document.getElementById("welcome").innerText =
            `Welcome ${data.username}`;

        document.getElementById("role").innerText =
            `Role: ${data.role}`;

        if (data.role === "admin") {
            document.getElementById("adminSection").style.display = "block";
}

    } catch (error) {
        console.error(error);
    }

});

async function getStats() {

    const token = localStorage.getItem("access");

    try {
        const response = await fetch("http://127.0.0.1:8000/users/dashboard/stats/", {
            headers: {
                "Authorization": `Bearer ${token}`
            }
        });

        const data = await response.json();

        //  نمایش در UI
        document.getElementById("totalUsers").innerText = data.Total_Users;
        document.getElementById("activeUsers").innerText = data.Active_Users;

    } catch (error) {
        console.error(error);

    }
}
getStats();

function toggleSellForm() {
    const form = document.getElementById("sellForm");

    if (form.style.display === "none") {
        form.style.display = "block";
    } else {
        form.style.display = "none";
    }
}