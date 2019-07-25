for i = 1:5 % 5' is Changeable. This is my matter.
    ii = i;
    while exist("param.txt",'file') == 0
        pause(1);
        ii = ii + 1
    end
    pause(10);

    par = importdata('param.txt');
    movefile('param.txt','param_'+num2str(i)+'.txt')

    MEX(par(1),par(2),par(3),par(4),par(5));

end