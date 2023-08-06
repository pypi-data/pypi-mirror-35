	.file	"daxpy.c"
	.text
	.p2align 4,,15
	.globl	daxpy
	.type	daxpy, @function
daxpy:
.LFB0:
	.cfi_startproc
	leaq	8(%rsp), %r10
	.cfi_def_cfa 10, 0
	movslq	%edi, %rax
	andq	$-32, %rsp
	pushq	-8(%r10)
	leaq	22(,%rax,8), %rdx
	pushq	%rbp
	.cfi_escape 0x10,0x6,0x2,0x76,0
	movq	%rsp, %rbp
	shrq	$4, %rdx
	pushq	%r12
	salq	$4, %rdx
	pushq	%r10
	.cfi_escape 0xf,0x3,0x76,0x70,0x6
	.cfi_escape 0x10,0xc,0x2,0x76,0x78
	pushq	%rbx
	subq	$24, %rsp
	.cfi_escape 0x10,0x3,0x2,0x76,0x68
	subq	%rdx, %rsp
	leaq	7(%rsp), %rcx
	subq	%rdx, %rsp
	leaq	7(%rsp), %r9
	shrq	$3, %rcx
	leaq	0(,%rcx,8), %rax
	shrq	$3, %r9
	leaq	0(,%r9,8), %rsi
	testl	%edi, %edi
	jle	.L12
	movq	%rax, %rdx
	shrq	$3, %rdx
	negq	%rdx
	andl	$3, %edx
	cmpl	%edi, %edx
	cmova	%edi, %edx
	cmpl	$4, %edi
	jg	.L28
	movl	%edi, %edx
.L3:
	vxorpd	%xmm0, %xmm0, %xmm0
	movl	$1, %r8d
	vmulsd	0(,%r9,8), %xmm0, %xmm0
	vaddsd	0(,%rcx,8), %xmm0, %xmm0
	vmovsd	%xmm0, 0(,%rcx,8)
	cmpl	$1, %edx
	je	.L5
	vxorpd	%xmm0, %xmm0, %xmm0
	movl	$2, %r8d
	vmulsd	8(,%r9,8), %xmm0, %xmm0
	vaddsd	8(,%rcx,8), %xmm0, %xmm0
	vmovsd	%xmm0, 8(,%rcx,8)
	cmpl	$2, %edx
	je	.L5
	vxorpd	%xmm0, %xmm0, %xmm0
	movl	$3, %r8d
	vmulsd	16(,%r9,8), %xmm0, %xmm0
	vaddsd	16(,%rcx,8), %xmm0, %xmm0
	vmovsd	%xmm0, 16(,%rcx,8)
	cmpl	$4, %edx
	jne	.L5
	vxorpd	%xmm0, %xmm0, %xmm0
	movl	$4, %r8d
	vmulsd	24(,%r9,8), %xmm0, %xmm0
	vaddsd	24(,%rcx,8), %xmm0, %xmm0
	vmovsd	%xmm0, 24(,%rcx,8)
.L5:
	cmpl	%edx, %edi
	je	.L12
.L4:
	leal	-1(%rdi), %r10d
	movl	%edi, %r11d
	movl	%edx, %r9d
	subl	%edx, %r11d
	subl	%edx, %r10d
	leal	-4(%r11), %ecx
	shrl	$2, %ecx
	addl	$1, %ecx
	leal	0(,%rcx,4), %ebx
	cmpl	$2, %r10d
	jbe	.L7
	salq	$3, %r9
	xorl	%edx, %edx
	xorl	%r10d, %r10d
	vxorpd	%xmm1, %xmm1, %xmm1
	leaq	(%rax,%r9), %r12
	addq	%rsi, %r9
        movl      $111, %ebx # INSERTED BY KERNCRAFT IACA MARKER UTILITY
        .byte     100        # INSERTED BY KERNCRAFT IACA MARKER UTILITY
        .byte     103        # INSERTED BY KERNCRAFT IACA MARKER UTILITY
        .byte     144        # INSERTED BY KERNCRAFT IACA MARKER UTILITY
.L8:
	vmovupd	(%r9,%rdx), %xmm0
	vinsertf128	$0x1, 16(%r9,%rdx), %ymm0, %ymm0
	vmulpd	%ymm1, %ymm0, %ymm0
	addl	$1, %r10d
	vaddpd	(%r12,%rdx), %ymm0, %ymm0
	vmovapd	%ymm0, (%r12,%rdx)
	addq	$32, %rdx
	cmpl	%r10d, %ecx
	ja	.L8
        movl      $222, %ebx # INSERTED BY KERNCRAFT IACA MARKER UTILITY
        .byte     100        # INSERTED BY KERNCRAFT IACA MARKER UTILITY
        .byte     103        # INSERTED BY KERNCRAFT IACA MARKER UTILITY
        .byte     144        # INSERTED BY KERNCRAFT IACA MARKER UTILITY
	addl	%ebx, %r8d
	cmpl	%ebx, %r11d
	je	.L23
	vzeroupper
.L7:
	movslq	%r8d, %rcx
	vxorpd	%xmm0, %xmm0, %xmm0
	leaq	(%rax,%rcx,8), %rdx
	vmulsd	(%rsi,%rcx,8), %xmm0, %xmm0
	vaddsd	(%rdx), %xmm0, %xmm0
	vmovsd	%xmm0, (%rdx)
	leal	1(%r8), %edx
	cmpl	%edx, %edi
	jle	.L12
	movslq	%edx, %rdx
	vxorpd	%xmm0, %xmm0, %xmm0
	addl	$2, %r8d
	leaq	(%rax,%rdx,8), %rcx
	vmulsd	(%rsi,%rdx,8), %xmm0, %xmm0
	vaddsd	(%rcx), %xmm0, %xmm0
	vmovsd	%xmm0, (%rcx)
	cmpl	%r8d, %edi
	jle	.L12
	movslq	%r8d, %r8
	vxorpd	%xmm0, %xmm0, %xmm0
	leaq	(%rax,%r8,8), %rdx
	vmulsd	(%rsi,%r8,8), %xmm0, %xmm0
	vaddsd	(%rdx), %xmm0, %xmm0
	vmovsd	%xmm0, (%rdx)
.L12:
	leaq	8(%rax), %rdi
	addq	$8, %rsi
	call	dummy@PLT
	leaq	-24(%rbp), %rsp
	popq	%rbx
	popq	%r10
	.cfi_remember_state
	.cfi_def_cfa 10, 0
	popq	%r12
	popq	%rbp
	leaq	-8(%r10), %rsp
	.cfi_def_cfa 7, 8
	ret
	.p2align 4,,10
	.p2align 3
.L28:
	.cfi_restore_state
	testl	%edx, %edx
	jne	.L3
	xorl	%r8d, %r8d
	jmp	.L4
	.p2align 4,,10
	.p2align 3
.L23:
	vzeroupper
	jmp	.L12
	.cfi_endproc
.LFE0:
	.size	daxpy, .-daxpy
	.ident	"GCC: (Debian 6.3.0-18+deb9u1) 6.3.0 20170516"
	.section	.note.GNU-stack,"",@progbits
