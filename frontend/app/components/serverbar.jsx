"use client";

import { useState, useEffect } from "react";

export default function ServerBar(props) {
    const [url, setUrl] = useState("");

    const setData = (data) => {
        props.setData(data);
    };

    const connectToServer = async () => {
        if (!url == "")
            try {
                const response = await fetch(`${url}/api/images`, {
                    method: "GET",
                    mode: "cors",
                    headers: {
                        "Content-Type": "application/json",
                    },
                });
                if (!response.ok) {
                    throw new Error("network not found");
                }
                const data = await response.json();

                setData(data);
            } catch (error) {
                console.error("Error connecting to the server:", error.message);
            }
    };

    useEffect(() => {
        const savedUrl = JSON.parse(localStorage.getItem("url"));
        if (savedUrl !== null) {
            setUrl(savedUrl);
            connectToServer();
        }
    }, [url]);

    return (
        <div className="w-full">
            <div className="relative flex max-w-lg gap-4 mx-auto">
                <span className="absolute inset-y-0 left-0 flex items-center pl-2">
                    <svg
                        fill="none"
                        height="24"
                        stroke="currentColor"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth="2"
                        viewBox="0 0 24 24"
                        width="24"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <circle cx="11" cy="11" r="8" />
                        <line x1="21" x2="16.65" y1="21" y2="16.65" />
                    </svg>
                </span>
                <input
                    className="block w-full py-2 pl-10 pr-3 leading-5 placeholder-gray-500 bg-white border border-gray-300 rounded-lg focus:outline-none focus:placeholder-gray-400 focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50"
                    type="text"
                    placeholder="Enter your image server URL"
                    value={url}
                    onChange={(e) => {
                        setUrl(e.target.value);
                        localStorage.setItem(
                            "url",
                            JSON.stringify(e.target.value),
                        );
                    }}
                />
                <button
                    className="px-4 py-2 font-bold text-white transition duration-300 bg-blue-500 rounded hover:bg-blue-600"
                    onClick={connectToServer}
                >
                    Connect
                </button>
            </div>
        </div>
    );
}
