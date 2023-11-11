/** @type {import('next').NextConfig} */
const nextConfig = {
    output: 'export',
    // when running in on github pages we need the basepath prefix, while locally we do not want that prefix
    basePath: process.env.NODE_ENV === "production" ? "/het-kirvin-project" : undefined,
}

module.exports = nextConfig
