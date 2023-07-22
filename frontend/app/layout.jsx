import "./globals.css";
import { Inter } from "next/font/google";
import Header from "./components/header.jsx";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
    title: "Animal Detection",
    description: "UI for camera & ML",
};

export default function RootLayout({ children }) {
    return (
        <html lang="en">
            <body className={inter.className}>
                <Header></Header>
                {children}
            </body>
        </html>
    );
}
