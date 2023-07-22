"use client";

import { useState, useEffect } from "react";
import Image from "next/image";
import Link from "next/link";

export default function Folder(props) {
    const [expand, setExpand] = useState(false);
    const handleClick = () => {
        setExpand((expand) => !expand);
    };

    useEffect(() => {
        console.log(props);
    });

    return (
        <div className="w-64">
            <button
                onClick={handleClick}
                className="transition duration-300 border-2 border-purple-400 border-opacity-0 rounded-md hover:border-opacity-50"
            >
                <Image
                    height="256"
                    width="256"
                    src={`data:image/png;base64,${props.species.images[0].image}`}
                    alt={props.species.species}
                    className="rounded-md aspect-video"
                />
                <p className="text-center">{props.species.species}</p>
            </button>
            <div
                className={`flex-wrap gap-4 justify-center mt-2 ${
                    expand ? "flex" : "hidden"
                }`}
            >
                {props.species.images.map((image, i) => {
                    return (
                        <Link key={i} href={`/images/${image.image_id}`}>
                            <Image
                                height="64"
                                width="64"
                                src={`data:image/png;base64,${image.image}`}
                                alt={image.species}
                                className="aspect-video"
                            />
                            <p className="text-center">{image.timestamp}</p>
                        </Link>
                    );
                })}
            </div>
        </div>
    );
}
