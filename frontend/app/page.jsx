"use client";

import ServerBar from "./components/serverbar";
import Folder from "./components/folder";
import { useState, useEffect } from "react";

export default function Home() {
    const [data, setData] = useState([]);
    const [species, setSpecies] = useState([]);
    useEffect(() => {
        let spc = {};
        for (const i in data) {
            const image = data[i];
            if (spc[image.species] === undefined) {
                spc[image.species] = [image];
            } else {
                spc[image.species].push(image);
            }
        }
        const arr = [];
        for (const key in spc) {
            arr.push({
                species: key,
                images: spc[key],
            });
        }

        setSpecies(arr);
    }, [data]);

    return (
        <main className="flex flex-col items-center justify-between p-12">
            <ServerBar setData={setData} />
            <div className="flex flex-wrap gap-4 my-4">
                {species.map((spcs, i) => (
                    <Folder species={spcs} key={i} />
                ))}
            </div>
        </main>
    );
}
