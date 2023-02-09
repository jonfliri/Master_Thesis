<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:xi="http://www.w3.org/2001/XInclude"
xmlns:ab="http://www.anybodytech.com"
                >
  <xsl:param name ="InstallPath">
    <xsl:value-of select="AnyScriptPackage/InstallPath"/>
  </xsl:param>

  <!--  <xsl:output
  method="xml|html|text|name"
  version="string"
  encoding="string"
  omit-xml-declaration="yes|no"
  standalone="yes|no"
  doctype-public="string"
  doctype-system="string"
  cdata-section-elements="namelist"
  indent="yes|no"
  media-type="string"/>
  -->
  <xsl:output
  method="xml"
  encoding="utf-8"
  indent="no"
  />

  <xsl:template match="/">
    <ab:anyml >

      <h1>
        <xsl:value-of select="AnyScriptPackage/Name"/>
      </h1>
      
      <xsl:copy-of select="AnyScriptPackage/Description/text() | AnyScriptPackage/Description/*"/>
      <br/>

      <ab:cmd>
        <xsl:attribute name="cmd">InstallDemoPackage <xsl:value-of select="AnyScriptPackage/ID"/></xsl:attribute>Install the demo repository by clicking this link.
      </ab:cmd>

    </ab:anyml>
  </xsl:template>


</xsl:stylesheet>