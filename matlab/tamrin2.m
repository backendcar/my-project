m = 6;
n = 6;

A = zeros(m,n);
for i = 1:m
    for j = 1:n
        A(i,j) = i + j;
    end
end
A