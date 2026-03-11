import Root, {
	type ButtonSize,
	type ButtonVariant,
	buttonVariants,
} from "./button.svelte";

import type { HTMLButtonAttributes, HTMLAnchorAttributes } from "svelte/elements";
import type { Snippet } from "svelte";

type ButtonProps = (HTMLButtonAttributes | HTMLAnchorAttributes) & {
	variant?: ButtonVariant;
	size?: ButtonSize;
	class?: string;
	href?: string;
	children?: Snippet;
};

export {
	Root,
	type ButtonProps as Props,
	//
	Root as Button,
	buttonVariants,
	type ButtonProps,
	type ButtonSize,
	type ButtonVariant,
};
