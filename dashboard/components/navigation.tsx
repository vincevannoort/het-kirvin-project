import { Navbar, NavbarBrand, NavbarContent, NavbarItem, Link, Button } from "@nextui-org/react";


export function Navigation() {
    return (
        <Navbar
            maxWidth='2xl'
            classNames={{ wrapper: "px-4" }}
            isBordered
        >
            <NavbarBrand>
                <p className="font-bold text-inherit">KIRVIN Project</p>
            </NavbarBrand>
            <NavbarContent className="hidden md:flex" justify="center">
                <NavbarItem>
                    <Link color="foreground" href="#temperature">
                        Temperature
                    </Link>
                </NavbarItem>
                <NavbarItem>
                    <Link color="foreground" href="#sunshine">
                        Sunshine
                    </Link>
                </NavbarItem>
                <NavbarItem>
                    <Link color="foreground" href="#rain">
                        Rain
                    </Link>
                </NavbarItem>
            </NavbarContent>
            <NavbarContent justify="end">
                <NavbarItem>
                    <Button as={Link} color="primary" href="https://github.com/vincevannoort/het-kirvin-project" variant="flat">
                        Source code
                    </Button>
                </NavbarItem>
            </NavbarContent>
        </Navbar>
    )
}