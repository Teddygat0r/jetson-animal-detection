"use client"

import Link from "next/link";
import { useState, useEffect } from "react";


export default function Header() {
    const [target, setTarget] = useState("");
    const [modal, setModal] = useState(false);

    const changeModal = () => {
        setModal(!modal);
    }

    return (
        <nav className="flex items-center py-8 text-lg font-bold text-gray-600 justify-evenly">
            <Link
                href="/"
                className="transition duration-300 border-b-2 border-gray-900 border-opacity-0 hover:text-gray-900 hover:border-opacity-100"
            >
                WildAEye
            </Link>
            <div className="flex gap-16">
                <Link
                    href="/"
                    className="transition duration-300 border-b-2 border-gray-900 border-opacity-0 hover:text-gray-900 hover:border-opacity-100"
                >
                    Home
                </Link>
                <button
                    href="/"
                    className="transition duration-300 border-b-2 border-gray-900 border-opacity-0 hover:text-gray-900 hover:border-opacity-100"
                    onClick = {
                        () => changeModal()
                    }
                >
                    Search

                </button>
            </div>
            <dialog className={`fixed top-[50%] translate-y-[-50%] left-0 bg-slate-200 flex-col gap-4 align-middle p-4 rounded-md ${ modal ? "flex" : "hidden" }`}>
                <input
                    className="block w-full py-2  px-3 leading-5 placeholder-gray-500 bg-white border border-gray-300 rounded-lg focus:outline-none focus:placeholder-gray-400 focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50"
                    type="text"
                    placeholder="Enter Image ID"
                    value={target}
                    onChange={(e) => {
                        setTarget(e.target.value);
                    }}
                />
                <Link href={`/images/${target}`} className="px-3 py-2 bg-blue-400 m-auto text-center rounded-md hover:bg-blue-500" onClick={() => changeModal()}>
                    Find
                </Link>
                
            </dialog>
        </nav>
    );
}
