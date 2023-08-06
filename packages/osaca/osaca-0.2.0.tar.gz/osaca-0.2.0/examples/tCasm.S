	.file	"taxCalc.c"
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"OSACA test start"
.LC3:
	.string	"OSACA test end"
	.section	.text.startup,"ax",@progbits
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB11:
	.cfi_startproc
	leaq	.LC0(%rip), %rdi
	subq	$4008, %rsp
	.cfi_def_cfa_offset 4016
	call	puts@PLT
	movl	$0x00000000, (%rsp)
	movss	4(%rsp), %xmm1
	movl	$2, %eax
	movss	.LC2(%rip), %xmm2
	movq	%rsp, %rdx
	.p2align 4,,10
	.p2align 3
.L2:
	pxor	%xmm0, %xmm0
	cvtsi2ss	%eax, %xmm0
	mulss	%xmm2, %xmm0
	addss	%xmm0, %xmm1
	movss	%xmm1, (%rdx,%rax,4)
	addq	$1, %rax
	cmpq	$1000, %rax
	jne	.L2
	leaq	3996(%rdx), %rdi
	call	dummy@PLT
	leaq	.LC3(%rip), %rdi
	call	puts@PLT
	xorl	%eax, %eax
	addq	$4008, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE11:
	.size	main, .-main
	.section	.rodata.cst4,"aM",@progbits,4
	.align 4
.LC2:
	.long	1044549468
	.ident	"GCC: (Debian 6.3.0-18) 6.3.0 20170516"
	.section	.note.GNU-stack,"",@progbits
