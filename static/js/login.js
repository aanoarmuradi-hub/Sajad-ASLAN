document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("#loginForm");

    if (!form) {
        console.error("Form not found!");
        return;
    }

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        console.log("clicked");

        const username = document.querySelector("#username").value;
        const password = document.querySelector("#password").value;

        try {
            const response = await fetch("https://aslan-store.onrender.com/api/token/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ username, password })
            });
            const data = await response.json();

            console.log(data);

            if (response.ok) {
                localStorage.setItem("access", data.access);
                const token = localStorage.getItem("access");

                const Response = await fetch("http://127.0.0.1:8000/users/user/info/", {
                    headers: {
                        "Authorization": `Bearer ${token}`
            }
            });
            const Data = await Response.json();
            if (Data.role === "user") {
                window.location.href = "/shop/dashboard/";

            }
             else {
                window.location.href = "/dashboard/";
            }

            }
           
        } catch (err) {
            console.error(err);
        }
    });
});