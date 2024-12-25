color("White", 1) {
    import("./KeyCap_Base.stl");
}
text_size = 5;
height = 0.01;
c = "center";
f = "Inter 18pt";
only_letter = false;

color("Blue", 1) {
    linear_extrude(height) {
        text("▶︎", size=text_size, valign=c, halign=c, font=f);
    }
}