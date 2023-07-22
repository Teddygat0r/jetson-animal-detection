import Link from "next/link";

export default function Header() {
    return (
        <nav className="flex items-center py-8 text-lg font-bold text-gray-600 justify-evenly">
            <Link
                href="/"
                className="transition duration-300 border-b-2 border-gray-900 border-opacity-0 hover:text-gray-900 hover:border-opacity-100"
            >
                Dinner
            </Link>
            <div className="flex gap-16">
                <Link
                    href="/"
                    className="transition duration-300 border-b-2 border-gray-900 border-opacity-0 hover:text-gray-900 hover:border-opacity-100"
                >
                    Home
                </Link>
                <Link
                    href="/camera"
                    className="transition duration-300 border-b-2 border-gray-900 border-opacity-0 hover:text-gray-900 hover:border-opacity-100"
                >
                    Camera
                </Link>
            </div>
        </nav>
    );
}
