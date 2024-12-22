color("White", 1) {
    import("../KeyCap_Base.stl");
}
text_size = 5;
text_shift_size = 4.5;
text_fn_size = 4;
height = 0.01;
c = "center";
f = "Inter 18pt";
only_letter = false;

linear_extrude(height) {
    translate([-3.7, 3.5, 0])
        text("LLT", size=text_shift_size, valign=c, halign=c, font=f);
    translate([-5.7, -3, 0])
        text("LLB", size=text_size, valign=c, halign="left", font=f);
    translate([3.5, 3.7, 0])
        text("LRT", size=text_fn_size, valign=c, halign=c, font=f);
}