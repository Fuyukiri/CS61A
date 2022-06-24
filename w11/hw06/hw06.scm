(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (sign num) 
    (cond 
    ((< num 0) -1)
    ((> num 0) 1)
    (else 0))
)

(define (square x) (* x x))

(define (pow x y) 
    (cond ((or (= x 0) (= x 1)) x)
          ((= y 1) x)
          ((= y 2) (square x))
          ((even? y) (square (pow x (/ y 2))))
          ((odd? y) (* x (square(pow x (quotient y 2)))))
    )
)
