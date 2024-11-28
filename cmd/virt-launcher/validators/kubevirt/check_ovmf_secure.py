loader = vl.dom_xpath("//domain/os/loader/text()")[0]
secure = vl.dom_xpath("//domain/os/loader/@secure")

if "secboot" in loader and secure != "yes":
    vl.add_warning(vl.WarningDomain_Domain, vl.WarningLevel_Notice,
                   "Secure OVMF code used without secure='yes'")
