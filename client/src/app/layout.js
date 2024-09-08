import "./globals.css";
import { Suspense } from "react";

export const metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body >
        <Suspense fallback={<div className=""></div>}>
          {/* <div className="bg-black w-screen h-screen z-50"><Image src="/images/offset.png" width={400} height={400}></Image></div> */}
          <main className="main-content">{children}</main>
        </Suspense>
      </body>
    </html>
  );
}

