A=zeros(12);
B=ones(5);
y=1;
x=1;

for y = 0:7
    for x = 0:7
        A(1+y:5+y,1+x:5+x)=B
        colormap gray
        imagesc(A)
        drawnow
        pause(1);
        A=zeros(12)
    end
end
