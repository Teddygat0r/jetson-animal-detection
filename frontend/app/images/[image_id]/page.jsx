"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import Image from "next/image";

export default function Page({ params }) {
    const [data, setData] = useState({});
    const router = useRouter();

    const queryData = async (savedUrl) => {
        console.log(`${savedUrl}/api/images/${params.image_id}`)
        try {
            const response = await fetch(
                `${savedUrl}/api/images/${params.image_id}`,
                {
                    method: "GET",
                    mode: "cors",
                    headers: {
                        "Content-Type": "application/json",
                    },
                },
            );
            if (!response.ok) {
                throw new Error("network not found");
            }
            const dt = await response.json();
            if (JSON.stringify(dt) == JSON.stringify({}))
                throw new Error("Image not found");
            setData(dt);
        } catch (error) {
            console.error("Error connecting to the server:", error.message);
            alert("Server not set");
            router.replace("/");
        }
    };
    useEffect(() => {
        const savedUrl = JSON.parse(localStorage.getItem("url"));
        queryData(savedUrl);
    }, []);

    return (
        <main className="flex flex-col items-center justify-between p-12">
            <div className="flex flex-col gap-4 my-4">
                <Image
                    width="1024"
                    height="1024"
                    src={`data:image/png;base64,${data.image}`}
                    alt={data.species}
                    className="aspect-video"
                />
                <p className="text-2xl font-bold text-center">{data.species}</p>
                <p className="text-lg text-center">
                    Taken at: {data.timestamp}
                </p>
            </div>
        </main>
    );
}
